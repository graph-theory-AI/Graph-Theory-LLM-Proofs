```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain sharp fixed-cap exponents, an additive-two window for private palettes, and the exact (2,3) boundary when Delta_A=2.",
  "would_publish": false,
  "caveats": "The full characterization is not obtained; the unrestricted factorial-factor gap persists, and literature novelty is not claimed."
}
```

# 1. Scope and results

All graphs below are finite and simple. Lists can be trimmed to the specified sizes.

The recursive forcing idea in the supplied attempt survives verification. Using **every intermediate target size** makes its error explicit. I also replace its local-lemma estimate with a slightly sharper, self-contained bound and extend the upper-bound argument to \(k_A<\Delta_A\).

Write
\[
s=\Delta_A,\qquad r=k_A,\qquad D=\Delta_B,\qquad q=k_B,
\]
where \(2\le r\le s\) and \(D,q\ge2\). Put
\[
c_r=\frac{(r-1)^{r-1}}{r^r},
\qquad
\lambda_r=c_r^{-1},
\qquad
C_{s,r}=\binom{s-1}{r-1}.
\]

The principal sufficient condition proved below is
\[
\boxed{\quad q^r\ge r!\lambda_r\bigl(DC_{s,r}-1\bigr).\quad}
\tag{1}
\]
Under (1), every bipartite graph with one-sided degree caps \(s,D\) is \((r,q)\)-choosable.

The obstruction is explicit. Define
\[
M_r(q)=
\max_{1\le t\le q}
\left\{(q-t)(t+1)^{r-1}+t^{r-1}\right\}.
\tag{2}
\]
There is a non-\((r,q)\)-choosable graph with
\[
\boxed{\quad \Delta_A=r,\qquad \Delta_B\le M_r(q)
       \le c_r(q+2)^r.\quad}
\tag{3}
\]
Moreover, its \(B\)-lists are pairwise disjoint.

Consequently, if
\[
F_{s,r}(D)=\min\{q\ge1:
 \text{every graph with caps }s,D\text{ is }(r,q)\text{-choosable}\},
\]
then, for fixed \(s,r\) and sufficiently large \(D\),
\[
\boxed{
\left\lfloor(\lambda_rD)^{1/r}\right\rfloor-1
\le F_{s,r}(D)
\le
\left\lceil
\bigl(r!\lambda_r(DC_{s,r}-1)\bigr)^{1/r}
\right\rceil .
}
\tag{4}
\]
In particular,
\[
F_{s,r}(D)=\Theta_{s,r}(D^{1/r}).
\tag{5}
\]
For fixed \(s,r\), the upper bound is at most \(D\) for all sufficiently large \(D\), so it lies in the catalog’s permitted range.

For the restricted class in which the \(B\)-lists are pairwise disjoint, the optimal list size is determined within **two integer values of uncertainty**: writing \(P_r(D)\) for that restricted threshold and
\[
u=(\lambda_rD)^{1/r},
\]
we obtain, whenever \(u\ge4\),
\[
\boxed{
\lfloor u\rfloor-1
\le P_r(D)
\le
\left\lceil(\lambda_r(D-1))^{1/r}\right\rceil
\le\lceil u\rceil .
}
\tag{6}
\]
This restricted threshold is independent of the cap \(s\), as long as \(s\ge r\).

Finally, an exact unrestricted small-list result is:
\[
\boxed{
\text{Every graph with }\Delta_A\le2,\ \Delta_B\le D
\text{ is }(2,3)\text{-choosable}
\iff D\le4.
}
\tag{7}
\]

These are partial results, not a characterization of the optimal pairs in Problem 3.

# 2. A self-contained local lemma for bounded supports

The following improves the finite denominator used in the supplied attempt.

## Lemma 1

Suppose events \(E_i\) are defined using independent random variables. Each event is supported on a specified set of exactly \(r\) variables, and each variable belongs to at most \(T\) supports, where \(r,T\ge2\).

If
\[
\Pr(E_i)\le p\le \frac{c_r}{T-1}
\qquad\text{for every }i,
\tag{8}
\]
then
\[
\Pr\left(\bigcap_i\overline{E_i}\right)>0.
\]

### Proof

We first establish the required positivity of an independence polynomial.

Let \(\mathcal H\) be the \(r\)-uniform multihypergraph whose vertices are the variables and whose indexed edges are the event supports. Repeated supports are allowed. For any such hypergraph of maximum degree at most \(T\), define
\[
Z(\mathcal H)=\sum_{\mathcal M}(-p)^{|\mathcal M|},
\]
where the sum is over matchings of indexed edges, including the empty matching.

Set
\[
x=\frac{r-1}{r}.
\]
Thus
\[
p\le \frac{x^{r-1}(1-x)}{T-1}.
\]

For a vertex \(v\), let \(\mathcal H-v\) mean deletion of \(v\) and every edge containing it. We prove by induction on the number of vertices that \(Z(\mathcal H)>0\), and that
\[
R_v(\mathcal H):=\frac{Z(\mathcal H)}{Z(\mathcal H-v)}>x
\quad\text{if }d_{\mathcal H}(v)\le T-1.
\tag{9}
\]

The case of no edges is immediate. Partitioning matchings according to whether they cover \(v\) gives
\[
Z(\mathcal H)
=
Z(\mathcal H-v)
-p\sum_{e\ni v}Z(\mathcal H-V(e)).
\tag{10}
\]
Fix \(e\ni v\), and write \(e\setminus\{v\}=\{w_1,\ldots,w_{r-1}\}\). Telescoping yields
\[
\frac{Z(\mathcal H-v)}{Z(\mathcal H-V(e))}
=
\prod_{j=1}^{r-1}
R_{w_j}\bigl(\mathcal H-v-w_1-\cdots-w_{j-1}\bigr).
\tag{11}
\]
Each \(w_j\) has lost at least the edge \(e\), so its degree in the corresponding hypergraph is at most \(T-1\). Every factor in (11) is therefore greater than \(x\), by induction.

If \(d(v)>0\) and \(p>0\), equations (10)–(11) imply
\[
R_v(\mathcal H)
>
1-\frac{d(v)p}{x^{r-1}}
\ge
1-\frac{d(v)}{r(T-1)}.
\tag{12}
\]
For \(d(v)\le T-1\), this is greater than or equal to \(x\), with strict inequality as required. For arbitrary \(d(v)\le T\), it is positive because
\[
r(T-1)\ge T,
\]
and the first inequality in (12) is strict. Isolated vertices and \(p=0\) are immediate. This proves the induction.

Now form the dependency graph \(H\) by joining events with intersecting supports. For \(S\subseteq V(H)\), put
\[
Q(S)=
\sum_{\substack{I\subseteq S\\ I\text{ independent in }H}}
(-p)^{|I|}.
\]
Independent sets of \(H[S]\) are precisely matchings in the corresponding support multihypergraph. Hence \(Q(S)>0\) for every \(S\).

For completeness, this positivity implies event avoidance as follows. Write
\[
P(S)=\Pr\left(\bigcap_{i\in S}\overline{E_i}\right).
\]
Inductively, for \(i\in S\),
\[
\frac{P(S)}{P(S\setminus\{i\})}
\ge
\frac{Q(S)}{Q(S\setminus\{i\})}>0.
\tag{13}
\]
Indeed, independence from non-neighbors gives
\[
P(S)\ge
P(S\setminus\{i\})-p\,P(S\setminus N_H[i]).
\]
Applying the induction hypothesis successively to the vertices in
\(N_H(i)\cap S\) gives
\[
\frac{P(S\setminus N_H[i])}{P(S\setminus\{i\})}
\le
\frac{Q(S\setminus N_H[i])}{Q(S\setminus\{i\})}.
\]
The recurrence
\[
Q(S)=Q(S\setminus\{i\})-p\,Q(S\setminus N_H[i])
\]
then proves (13). Taking \(S=V(H)\) finishes the proof. ∎

# 3. Applying the lemma to arbitrary lists

Independently and uniformly choose
\[
\phi(b)\in L(b)
\qquad(b\in B).
\]

For every \(a\in A\) and every \(r\)-element subset \(S\subseteq N(a)\), define \(E_{a,S}\) to be the event that the colors on \(S\) are exactly the \(r\) distinct colors of \(L(a)\).

There are at most \(r!\) assignments realizing this event, so
\[
\Pr(E_{a,S})\le\frac{r!}{q^r}.
\tag{14}
\]

A variable \(\phi(b)\) is involved in at most
\[
\sum_{a\in N(b)}
\binom{d(a)-1}{r-1}
\le
D\binom{s-1}{r-1}
=DC_{s,r}
\tag{15}
\]
events. Lemma 1 therefore applies under (1).

Avoiding all these events ensures that no \(A\)-vertex is blocked: if all \(r\) colors of \(L(a)\) appeared on its neighbors, choosing one witness neighbor for each color would produce an event \(E_{a,S}\). Thus every \(a\) retains an available color. Since \(A\) is independent, we can finish the coloring.

This proves (1).

## Private \(B\)-palettes

Suppose now that distinct vertices in \(B\) have disjoint lists.

For a fixed \(a\), each color in \(L(a)\) has at most one possible owner in \(B\). The event that \(a\) is blocked is impossible unless:

1. every color in \(L(a)\) has an owner in \(N(a)\); and
2. these \(r\) owners are distinct.

When both conditions hold, blocking \(a\) is one prescribed assignment on exactly \(r\) variables, of probability \(q^{-r}\). Each variable occurs in at most \(D\) such events. Lemma 1 gives the sufficient condition
\[
\boxed{\quad q^r\ge\lambda_r(D-1).\quad}
\tag{16}
\]

This also explains why the cap on \(A\) becomes irrelevant in this restricted class. An automatically safe \(A\)-vertex can be left until the end; for every other \(A\)-vertex, all edges except those to its \(r\) owners are irrelevant. The problem reduces exactly to one with \(A\)-degrees at most \(r\).

# 4. The explicit forcing obstruction

All \(B\)-vertices in this construction have pairwise disjoint \(q\)-element palettes.

For every \(t\in\{1,\ldots,q\}\), construct a rooted gadget \(H_t\), whose root \(x\in B\) has a designated subset
\[
S_x\subseteq L(x),\qquad |S_x|=t.
\]
The gadget will force \(x\) to use a color in \(S_x\).

For \(t=q\), take only the root.

Suppose \(H_{t+1}\) has been constructed. For each
\[
c\in L(x)\setminus S_x,
\]
take \(r-1\) fresh copies of \(H_{t+1}\), with roots
\[
y_{c,1},\ldots,y_{c,r-1}
\]
and designated target sets \(T_{c,j}\), each of size \(t+1\).

For every tuple
\[
(d_1,\ldots,d_{r-1})
\in T_{c,1}\times\cdots\times T_{c,r-1},
\]
add an \(A\)-vertex adjacent to
\[
x,y_{c,1},\ldots,y_{c,r-1},
\]
with list
\[
\{c,d_1,\ldots,d_{r-1}\}.
\tag{17}
\]
These are \(r\) distinct colors.

## Forcing property

Every coloring of \(H_t\) gives its root a color in \(S_x\). Conversely, every root color in \(S_x\) extends to a coloring of \(H_t\).

This follows by downward induction on \(t\). If \(x\) uses a forbidden color \(c\), the helper roots use some tuple from their designated target sets. The connector corresponding to that tuple has every list color used on its neighbors, a contradiction.

Conversely, if \(x\in S_x\), color all helper gadgets inductively. Every connector associated with the forbidden color \(c\) can itself use \(c\): neither \(x\) nor any helper root uses that color. ∎

## Closing the construction

Take \(r\) disjoint copies of \(H_1\). Their roots are forced to distinct private colors
\[
\alpha_1,\ldots,\alpha_r.
\]
Add one final \(A\)-vertex adjacent to these roots, with list
\[
\{\alpha_1,\ldots,\alpha_r\}.
\]
It is blocked in every coloring.

## Degree calculation

A root of \(H_t\) has
\[
(q-t)(t+1)^{r-1}
\]
incident connectors inside its gadget.

If it occurs as a helper in its parent gadget, it has an additional
\[
t^{r-1}
\]
incident connectors. The top-level \(H_1\) roots receive one final connector, also equal to \(1^{r-1}\). A leaf root \(H_q\) has only its \(q^{r-1}\) parent connectors.

Thus every \(B\)-degree is at most \(M_r(q)\) from (2), and every \(A\)-degree is exactly \(r\).

Finally,
\[
\begin{aligned}
(q-t)(t+1)^{r-1}+t^{r-1}
&\le (q-t+1)(t+1)^{r-1}\\
&\le
\max_{0\le z\le q+2}(q+2-z)z^{r-1}\\
&=c_r(q+2)^r.
\end{aligned}
\tag{18}
\]
This proves (3).

The construction is finite and gives a simple bipartite graph. Different connector vertices may have identical neighborhoods, but no parallel graph edges are introduced.

# 5. Quantitative consequences

Let \(D_r^{\mathrm{priv}}(q)\) be the least maximum \(B\)-degree of a private-palette counterexample with \(A\)-lists of size \(r\). The reduction in Section 3 shows that allowing \(A\)-degree greater than \(r\) does not change this threshold.

The sufficient condition (16) and the construction give
\[
\boxed{
1+c_rq^r
<
D_r^{\mathrm{priv}}(q)
\le M_r(q)
\le c_r(q+2)^r.
}
\tag{19}
\]
In particular, for fixed \(r\),
\[
D_r^{\mathrm{priv}}(q)
=c_rq^r+O_r(q^{r-1}).
\tag{20}
\]

To obtain (6), put \(u=(\lambda_rD)^{1/r}\). The upper bound follows from (16). For the lower bound, take
\[
q_0=\lfloor u\rfloor-2.
\]
If \(u\ge4\), then \(q_0\ge2\), and
\[
M_r(q_0)\le c_r(q_0+2)^r\le c_ru^r=D.
\]
Thus \(q_0\) does not suffice, proving
\[
P_r(D)\ge q_0+1=\lfloor u\rfloor-1.
\]

The same obstruction is valid without the private-palette restriction. Combining it with (1) proves (4)–(5). In particular,
\[
\lambda_r^{1/r}
\le
\liminf_{D\to\infty}\frac{F_{s,r}(D)}{D^{1/r}}
\le
\limsup_{D\to\infty}\frac{F_{s,r}(D)}{D^{1/r}}
\le
(r!\lambda_r C_{s,r})^{1/r}.
\tag{21}
\]

When \(s=r\), the remaining multiplicative gap is \((r!)^{1/r}\), just as in the supplied attempt. The improvement here is in the finite error, the local-lemma denominator, and the extension to all fixed \(s\ge r\).

# 6. The exact \((2,3)\) boundary for \(\Delta_A=2\)

We use an elementary orientation criterion.

## Lemma 2

A bipartite graph with degree caps \(\Delta_A,\Delta_B\) is \((k_A,k_B)\)-choosable if
\[
\frac{k_A-1}{\Delta_A}
+
\frac{k_B-1}{\Delta_B}
\ge1.
\tag{22}
\]

### Proof

First orient the edges so that
\[
d^+(a)\le k_A-1,\qquad d^+(b)\le k_B-1.
\tag{23}
\]
Such an orientation exists by the capacitated form of Hall’s theorem. Indeed, for every vertex set \(W\), writing \(m=e(G[W])\), we have
\[
|W\cap A|\ge\frac m{\Delta_A},
\qquad
|W\cap B|\ge\frac m{\Delta_B}.
\]
Therefore
\[
(k_A-1)|W\cap A|+(k_B-1)|W\cap B|\ge m.
\]
Assigning every edge to one endpoint, with the indicated endpoint capacities, is a bipartite matching problem; these inequalities imply Hall’s condition. Direct each edge away from its assigned endpoint.

Every orientation of a bipartite graph has a kernel: an independent set \(K\) such that every vertex outside \(K\) has an outgoing arc into \(K\). Here is a direct construction. Start with \(K=A\). Whenever \(b\in B\setminus K\) has no outgoing arc into \(K\), add \(b\) to \(K\) and remove all its neighbors currently in \(K\cap A\). Each removed \(A\)-vertex points to this \(b\), which is never subsequently removed. At termination, \(K\) is independent and has the required absorption property. The same argument applies to every induced subgraph.

Now choose a color \(c\), and take a kernel in the subgraph induced by vertices whose lists contain \(c\). Color that kernel with \(c\), delete its vertices, and remove \(c\) from all remaining lists. Every uncolored vertex losing \(c\) also loses an outgoing neighbor. Hence the invariant
\[
|L(v)|\ge d^+(v)+1
\]
is preserved. Induction completes the coloring. ∎

Apply (22) with
\[
\Delta_A=2,\quad k_A=2,\quad k_B=3.
\]
It holds whenever \(D\le4\), because
\[
\frac12+\frac2D\ge1.
\]

For the converse, formula (2) simplifies when \(r=2\):
\[
\begin{aligned}
M_2(q)
&=\max_{1\le t\le q}\{-t^2+qt+q\}\\
&=\left\lfloor\frac{q^2}{4}\right\rfloor+q.
\end{aligned}
\tag{24}
\]
Thus
\[
M_2(3)=5.
\]
The construction in Section 4 supplies a non-\((2,3)\)-choosable graph with \(\Delta_A=2\), \(\Delta_B\le5\). It remains a counterexample for every larger cap \(D\).

This proves (7). Likewise \(M_2(2)=3\), recovering the exact \((2,2)\) boundary.

# 7. An additional obstruction involving both degree caps

The forcing construction is particularly effective when \(s\) is small. A different explicit family shows why the dependence on \(s\) cannot disappear in the unrestricted problem.

Fix positive integers \(\ell,h\). For each \(j\in[\ell]\), take \(r\) pairwise disjoint color classes
\[
X_{j,1},\ldots,X_{j,r},
\qquad |X_{j,i}|=h,
\]
with all classes globally disjoint.

Create \(r^\ell\) vertices in \(B\), indexed by
\[
(i_1,\ldots,i_\ell)\in[r]^\ell,
\]
and give that vertex the list
\[
X_{1,i_1}\cup\cdots\cup X_{\ell,i_\ell}.
\]
Every \(B\)-list has size \(q=\ell h\).

For each \(j\), create an \(A\)-vertex for every choice of one color from each of
\[
X_{j,1},\ldots,X_{j,r},
\]
giving it those \(r\) colors as its list. Join every \(A\)-vertex to every \(B\)-vertex. The graph is
\[
K_{\ell h^r,\ r^\ell},
\]
with
\[
\Delta_A=r^\ell,\qquad \Delta_B=\ell h^r.
\]

Suppose a coloring existed, and let \(U\) be the set of colors used on \(B\). For each \(j\), at least one class \(X_{j,i_j}\) must be disjoint from \(U\). Otherwise, choosing a used color from each of its \(r\) classes would give an \(A\)-list contained in \(U\), impossible in a complete bipartite graph.

But the \(B\)-vertex indexed by \((i_1,\ldots,i_\ell)\) then has its entire list disjoint from \(U\), a contradiction.

Thus
\[
\boxed{
r^\ell\le s,\qquad \ell h^r\le D
\quad\Longrightarrow\quad
(s,D)\text{ does not universally permit }(r,\ell h).
}
\tag{25}
\]

For fixed \(s,r\), this supplements (21) with
\[
\liminf_{D\to\infty}\frac{F_{s,r}(D)}{D^{1/r}}
\ge
\max\left\{
\lambda_r^{1/r},
\left\lfloor\log_r s\right\rfloor^{1-1/r}
\right\}.
\tag{26}
\]

In the symmetric degree-cap regime \(s=D=\Delta\), with \(r\) fixed, it gives
\[
F_{\Delta,r}(\Delta)
\ge
(1-o(1))\,
\Delta^{1/r}(\log_r\Delta)^{1-1/r}.
\tag{27}
\]
This demonstrates explicitly the necessity of a logarithmic factor in that regime, but does not provide a matching universal upper bound.

# 8. What remains unresolved

1. **Arbitrary overlapping lists remain the main obstruction.**  
   Even when \(k_A=\Delta_A=r\) is fixed, these arguments leave the factor \((r!)^{1/r}\) between the unrestricted upper and lower constants.

2. **The fixed-cap exponent does not settle the growing-cap regimes.**  
   The factor \(\binom{s-1}{r-1}\) in (1) makes that bound ineffective in much of the nearly symmetric parameter space.

3. **The private-palette conclusion is a genuine restriction.**  
   It gives an additive-two window and an explicit finite obstruction, but does not justify treating private palettes as extremal among arbitrary list assignments.

4. **No literature novelty is claimed.**  
   The arguments above are self-contained, but I have not verified their overlap with all general criteria in the source paper or subsequent work. The full set of optimal list-size pairs is not characterized here.