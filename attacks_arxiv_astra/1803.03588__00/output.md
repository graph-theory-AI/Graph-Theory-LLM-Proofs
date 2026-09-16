```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain an explicit polynomial bound for every cograph H and determine the exact maximum-degree bound for H = P3, but do not resolve arbitrary H.",
  "would_publish": false,
  "caveats": "Self-contained special cases only; no novelty or general resolution is claimed."
}
```

## 1. Formulation and partial results

All graphs below are finite and simple, and **\(H\)-free means induced-\(H\)-free**.

Call a nonempty set \(S\subseteq V(G)\) **\(d\)-restricted** if
\[
\Delta(G[S])\le d|S|
\quad\text{or}\quad
\Delta(\overline G[S])\le d|S|.
\]
I work with this maximum-degree version of Rödl’s theorem. Its polynomial-dependence question is equivalent, up to constant changes of parameters, to the edge-density version.

For \(0<d<1/2\), define the optimal guaranteed fraction
\[
\rho_H(d)=
\inf_{\substack{G\text{ is }H\text{-free}\\ |G|\ge1}}
\ \max_{\substack{\varnothing\ne S\subseteq V(G)\\ S\text{ is }d\text{-restricted}}}
\frac{|S|}{|G|}.
\]
The conjecture asks whether, for every fixed \(H\), there are \(c_H,C_H>0\) such that
\[
\rho_H(d)\ge c_Hd^{C_H}.
\]

Here are two unconditional special-case results, proved below.

**Theorem A.** If \(H\) is a cograph on \(h\ge2\) vertices, then
\[
\boxed{\displaystyle
\rho_H(d)\ge \frac12\left(\frac d8\right)^{2^h-2}.}
\]
Here a cograph is a graph constructed from single vertices by repeated disjoint unions and complete joins. It is the **forbidden graph \(H\)** that is assumed to be a cograph; \(G\) is otherwise arbitrary.

**Theorem B.** Let \(P_3\) be the three-vertex path and put
\[
r=\left\lceil\frac1d\right\rceil-1.
\]
Then the exact optimal fraction in the maximum-degree formulation is
\[
\boxed{\displaystyle
\rho_{P_3}(d)=\frac{1}{1+r(1-d)}.}
\]
In particular,
\[
\rho_{P_3}(d)=(1+O(d))d\qquad(d\to0).
\]

No novelty is claimed for these special cases. The general conjecture is not proved here.

---

## 2. Proof of Theorem A

### 2.1. A pruning observation

**Lemma 1.** If a graph \(F\) on \(m\ge1\) vertices satisfies
\[
e(F)\le \frac d8m^2,
\]
then it contains \(S\) with \(|S|\ge m/2\) and
\[
\Delta(F[S])\le d|S|.
\]

**Proof.** Delete every vertex whose degree in \(F\) exceeds \(dm/2\). Since
\[
\sum_{v\in V(F)}\deg_F(v)\le \frac d4m^2,
\]
fewer than \(m/2\) vertices are deleted. The remaining set \(S\) satisfies
\[
\Delta(F[S])\le dm/2\le d|S|.
\]
\(\square\)

Consequently, if \(G\) has no \(d\)-restricted set of size at least \(\delta n\), then every \(U\subseteq V(G)\) with \(|U|\ge2\delta n\) satisfies
\[
e(G[U])>\frac d8|U|^2,
\qquad
e(\overline G[U])>\frac d8|U|^2.
\tag{1}
\]

The main point is that this two-sided local density condition forces every fixed cograph, with polynomial quantitative bounds.

### 2.2. Counting cographs under two-sided local density

Fix a binary construction of a cograph \(H\). Define an integer \(B(H)\) recursively:

- \(B(K_1)=0\);
- if \(H\) is the disjoint union or complete join of \(H_1,H_2\), where
  \[
  |H_1|=a,\qquad |H_2|=b,
  \]
  set
  \[
  B(H)=B(H_2)+b\bigl(B(H_1)+a+1\bigr).
  \tag{2}
  \]

Either ordering of the children may be used. Copies in the following lemma are counted as injective induced embeddings from the fixed labeled vertex set of \(H\).

**Lemma 2.** Let \(0<q<1/4\) and \(L>0\). Suppose that a graph \(F\) satisfies
\[
e(F[U])>q|U|^2,
\qquad
e(\overline F[U])>q|U|^2
\tag{3}
\]
whenever \(|U|\ge L\). If
\[
|X|\ge Lq^{-B(H)},
\]
then \(F[X]\) contains at least
\[
q^{B(H)}|X|^{|H|}
\]
labeled induced copies of \(H\).

**Proof.** Induct on the chosen construction of \(H\). The assertion for \(K_1\) is immediate.

Suppose that \(H\) is obtained from \(H_1,H_2\) as in (2). Write
\[
B_i=B(H_i),\qquad P=B_1+a,\qquad
B=B_2+b(P+1),
\]
and let \(m=|X|\).

Let \(J=F\) if the operation is complete join, and \(J=\overline F\) if it is disjoint union. For \(v\in X\), put
\[
D_v=N_J(v)\cap X.
\]
Since \(e(J[X])>qm^2\), the vertices with \(|D_v|\ge qm\) satisfy
\[
\sum_{\substack{v\in X\\ |D_v|\ge qm}}|D_v|>qm^2.
\tag{4}
\]

We have \(B\ge B_1+1\). Thus, for every vertex counted in (4),
\[
|D_v|\ge qm\ge Lq^{-B_1}.
\]
Applying the induction hypothesis to \(H_1\) inside the **original graph** \(F[D_v]\), and then convexity, shows that the number \(I\) of pairs consisting of a vertex \(v\) and a labeled induced \(H_1\) in \(D_v\) satisfies
\[
\begin{aligned}
I
&\ge q^{B_1}
  \sum_{\substack{v\in X\\ |D_v|\ge qm}}|D_v|^a\\
&\ge q^{B_1}\frac{(qm^2)^a}{m^{a-1}}
 =q^Pm^{a+1}.
\end{aligned}
\tag{5}
\]

For each labeled induced copy \(A\) of \(H_1\) in \(F[X]\), let
\[
T_A=X\cap\bigcap_{x\in V(A)}N_J(x).
\]
These are open neighborhoods, so \(T_A\cap V(A)=\varnothing\). Double-counting gives
\[
I=\sum_A |T_A|.
\]

There are at most \(m^a\) such copies \(A\). Discard those for which
\[
|T_A|<q^{P+1}m.
\]
By (5), the retained copies satisfy
\[
\sum_{\text{retained }A}|T_A|
\ge (1-q)q^Pm^{a+1}
\ge q^{P+1}m^{a+1}.
\tag{6}
\]

Since \(B\ge B_2+P+1\), each retained \(T_A\) has
\[
|T_A|\ge q^{P+1}m\ge Lq^{-B_2}.
\]
The induction hypothesis supplies at least
\[
q^{B_2}|T_A|^b
\]
labeled induced copies of \(H_2\) in \(F[T_A]\).

Every such pair of copies forms an induced \(H\): all cross-pairs have exactly the required adjacency, by the definition of \(J\) and \(T_A\). Using (6) and convexity once more, the number of induced \(H\)'s is at least
\[
\begin{aligned}
q^{B_2}\sum_{\text{retained }A}|T_A|^b
&\ge
q^{B_2}
\frac{\bigl(q^{P+1}m^{a+1}\bigr)^b}{(m^a)^{b-1}}\\
&=q^{B_2+b(P+1)}m^{a+b}\\
&=q^Bm^{|H|}.
\end{aligned}
\]
This completes the induction. \(\square\)

### 2.3. Bounding the exponent

For every construction of an \(h\)-vertex cograph,
\[
B(H)\le 2^h-2.
\tag{7}
\]
Indeed, the induction step gives
\[
B(H)\le 2^b-2+b(2^a+a-1)\le 2^{a+b}-2.
\]
For the last inequality, observe that
\[
\begin{aligned}
&2^{a+b}-\bigl(2^b+b(2^a+a-1)\bigr)\\
&\qquad=2^a(2^b-b)-2^b-b(a-1)\\
&\qquad\ge a(2^b-2b)\ge0,
\end{aligned}
\]
using \(2^a\ge a+1\) and \(2^b\ge2b\).

### 2.4. Applying the counting lemma

Set
\[
q=d/8,\qquad
\delta=\frac12q^{B(H)}.
\]
Suppose an \(H\)-free graph \(G\) on \(n\ge1\) vertices had no \(d\)-restricted set of size at least \(\delta n\).

By Lemma 1, condition (3) would hold with
\[
L=2\delta n=q^{B(H)}n.
\]
Lemma 2, applied to \(X=V(G)\), would then give at least
\[
q^{B(H)}n^h>0
\]
induced copies of \(H\), a contradiction.

Thus
\[
\rho_H(d)\ge \frac12(d/8)^{B(H)}.
\]
Combining this with (7) proves Theorem A. No lower bound on \(n\) was required.

---

## 3. Proof of the exact bound for \(P_3\)

A graph is induced-\(P_3\)-free exactly when it is a disjoint union of cliques: a connected noncomplete component would contain a shortest path whose first three vertices induce \(P_3\).

Put
\[
r=\left\lceil\frac1d\right\rceil-1,\qquad
\gamma=1-rd,\qquad
M=\frac1{r+\gamma}.
\]
Then
\[
rd<1\le(r+1)d,\qquad 0<\gamma\le d,
\]
and
\[
M=\frac1{1+r(1-d)}.
\]

### 3.1. Universal lower bound

Let \(G\) be a disjoint union of cliques of sizes \(a_1,\dots,a_\ell\), with total order \(n\). Set
\[
s=\lceil Mn\rceil.
\]
If some \(a_i\ge s\), a clique of size \(s\) is \(d\)-restricted. Hence assume
\[
a_i\le s-1\qquad\text{for every }i.
\]

Put
\[
k=\lfloor ds\rfloor+1.
\]
It suffices to prove
\[
\sum_i\min(a_i,k)\ge s.
\tag{8}
\]
Indeed, we can then select exactly \(s\) vertices, at most \(k\) from each component, obtaining maximum degree at most
\[
k-1=\lfloor ds\rfloor\le ds.
\]

If \(k\ge s-1\), (8) is immediate. Otherwise, if at least \(r+1\) components have size greater than \(k\), then
\[
\sum_i\min(a_i,k)\ge(r+1)k>(r+1)ds\ge s.
\]

In the remaining case, at most \(r\) components have size greater than \(k\). Consequently,
\[
\sum_i\min(a_i,k)
\ge n-r(s-1-k).
\]
Since \(s-1<Mn\), we have \(n>(r+\gamma)(s-1)\), and therefore
\[
\begin{aligned}
n-r(s-1-k)
&>\gamma(s-1)+rk\\
&>\gamma(s-1)+rds\\
&=s-\gamma>s-1.
\end{aligned}
\]
The left-hand side of (8) is an integer, proving (8). Thus every \(P_3\)-free graph has a \(d\)-restricted set of size at least \(Mn\), so
\[
\rho_{P_3}(d)\ge M.
\]

### 3.2. Matching extremal sequence

For sufficiently large integers \(T\), let
\[
b_T=\lfloor\gamma T\rfloor-r>0,
\]
and let \(G_T\) be the disjoint union of \(r\) cliques of size \(T\) and one clique of size \(b_T\). Its order is
\[
n_T=rT+b_T.
\]

First, any \(d\)-dense set lies in one component. Indeed, if such a set \(S\) meets a component in \(s_i>0\) vertices, then
\[
|S|-s_i\le d|S|,
\]
so \(s_i\ge(1-d)|S|\). Two nonempty intersections are impossible because \(d<1/2\). Hence every \(d\)-dense set has size at most \(T\).

Now let \(S\) be \(d\)-sparse, with \(x=|S|\). Its intersection with each of the \(r\) large cliques has size at most \(dx+1\). Thus
\[
x\le r(dx+1)+b_T,
\]
and consequently
\[
\gamma x\le r+b_T=\lfloor\gamma T\rfloor\le\gamma T.
\]
So \(x\le T\).

A clique of size \(T\) is itself \(d\)-restricted. Therefore the largest \(d\)-restricted set in \(G_T\) has size exactly \(T\), and
\[
\rho_{P_3}(d)
\le\lim_{T\to\infty}\frac{T}{rT+b_T}
=\frac1{r+\gamma}=M.
\]
This proves Theorem B, including all rounding issues.

Since \(r=d^{-1}+O(1)\), it follows that
\[
\rho_{P_3}(d)=(1+O(d))d.
\]

### A general necessary bound

Complementation preserves restricted sets, so
\[
\rho_{\overline H}(d)=\rho_H(d).
\]
Also, if \(H\) contains an induced \(F\), then \(\rho_H(d)\le\rho_F(d)\).

Every graph having both an edge and a nonedge contains an induced \(P_3\) or \(\overline{P_3}\). Consequently, for every such \(H\),
\[
\boxed{\displaystyle
\rho_H(d)\le
\frac1{1+(\lceil1/d\rceil-1)(1-d)}
=(1+O(d))d.}
\]
In particular, a polynomial lower bound \(c_Hd^{C_H}\) for such an \(H\) cannot have exponent \(C_H<1\).

---

## 4. Connection to Erdős–Hajnal and the remaining gap

For completeness, suppose the conjectured bound
\[
\rho_H(d)\ge c_Hd^{C_H}
\]
were available for a fixed \(H\). For sufficiently large \(n\), choose
\[
d=(c_Hn)^{-1/(C_H+1)}.
\]
The restricted set supplied by the bound has size
\[
m\ge(c_Hn)^{1/(C_H+1)}.
\]
Greedy coloring in its sparse orientation gives a clique or independent set in \(G\) of size at least
\[
\frac{m}{dm+1}
\ge \frac12(c_Hn)^{1/(C_H+1)}.
\]
After decreasing the exponent to absorb constants and small orders, this gives the Erdős–Hajnal property for \(H\).

The unresolved step in the present attack is precise: Lemma 2 works because, at every stage, **all cross-pairs between the two pieces of the forbidden graph have the same adjacency**. Common neighborhoods or common antineighborhoods then enforce the entire cross-pattern. A general forbidden graph need not admit such a recursive decomposition, and this argument provides no replacement that handles mixed cross-adjacencies with polynomial losses.

Thus the writeup establishes explicit polynomial bounds for a structural family and a sharp extremal special case, but neither proves nor disproves polynomial Rödl dependence for arbitrary \(H\).