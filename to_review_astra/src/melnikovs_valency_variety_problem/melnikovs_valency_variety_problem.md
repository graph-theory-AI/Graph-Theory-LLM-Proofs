---
title: 'Melnikov''s valency-variety problem'
subtitle: 'Unrefereed candidate disproof by GPT-6 Astra'
author:
  - 'Writeup: `gpt-6-astra` (single model pass)'
date: 'Catalog id `melnikovs_valency_variety_problem` — generated 2026-09-16'
---

::: {.warning}
**UNREFEREED MODEL OUTPUT.** This document was selected solely because GPT-6 Astra labelled its own result `would_publish: true` and returned `proved` or `disproved`. It has not passed the adversarial LLM referee used for the earlier Sol campaign, has not been checked by a human mathematician, and has not been checked for novelty. Treat every mathematical and bibliographic claim below as unverified.
:::

# Summary and provenance

| | |
|:--|:--|
| Catalog id | `melnikovs_valency_variety_problem` |
| Catalog entry | [Melnikov's valency-variety problem](https://graph-theory-ai.github.io/graph-conjectures/op/melnikovs_valency_variety_problem/) |
| Source corpus | opg |
| Campaign leg | OpenProblemGarden first pass (`attacks_opg`) |
| Source paper / entry | http://www.openproblemgarden.org/op/melnikovs_valency_variety_problem |
| Model verdict | **disproved** (confidence: high) |
| Model's one-line claim | A 37-vertex graph has chromatic number 3 and degree set {0,1,...,29}, making the proposed right-hand side equal to 3; moreover, 37 vertices is minimum. |
| Model | `gpt-6-astra`, reasoning effort `max`, `mode=pro`, flex service tier |
| Original artifact | `attacks_opg/melnikovs_valency_variety_problem/output.md` |
| Independent review | **None** |
| Model's caveats | The counterexample has one isolated vertex, which the statement permits; bibliographic novelty has not been independently checked. |

# Problem statement

Problem The valency-variety $w(G)$ of a graph $G$ is the number of different degrees in $G$ . Is the chromatic number of any graph $G$ with at least two vertices greater than $$\ceil{ \frac{\floor{w(G)/2}}{|V(G)| - w(G)} } ~ ?$$

## Catalog context

According to Jensen and Toft [JT, p. 90], the problem is due to Melnikov and was mentioned by Vizing [V] and Zykov [Z]. According to Zykov [Z], Melnikov showed that the suggested lower bound would be best possible. A best possible upper bound on the chromatic number in terms of $|V(G)|$ and $w(G)$ is $|V(G)| - \floor{ w(G) / 2 }$ as proved by Nettleton [N] and Dirac [D].

# Astra writeup

*The text below is the model output verbatim, apart from moving its machine-readable verdict block into the summary above and shifting Markdown heading levels for this document. Mechanical TeX defects and equation tags were normalized where needed for compilation.*

## A smallest counterexample

Graphs below are finite and simple, and degree \(0\) counts toward the valency-variety.

### 1. Explicit construction

Take disjoint vertex sets
\begin{equation*}
\begin{aligned}
A&=\{a_1,\ldots,a_5\},&
B&=\{b_0,\ldots,b_5\},\\
C&=\{c_0,\ldots,c_6\},&
T&=\{t_1,\ldots,t_6\},\\
U&=\{u_1,\ldots,u_{12}\},
\end{aligned}
\end{equation*}
together with one vertex \(z\). There are
\[
5+6+7+6+12+1=37
\]
vertices.

Define the edges as follows, with **no edges other than those specified**.

1. On \(A\cup B\cup C\), put the complete tripartite graph with parts \(A,B,C\).

2. Join every vertex of \(T\) to every vertex of \(B\cup C\).

3. Join each of \(u_7,\ldots,u_{12}\) to every vertex of \(B\).

4. Put the following edges between \(U\) and \(A\):
   \begin{equation*}
\begin{aligned}
   N(u_7)\cap A&=\{a_5\},\\
   N(u_8)\cap A&=\{a_4,a_5\},\\
   N(u_9)\cap A&=\{a_3,a_4,a_5\}.
   \end{aligned}
\end{equation*}

5. For \(i\in\{10,11,12\}\), join \(u_i\) to \(c_j\) precisely when
   \[
   j\ge 13-i.
   \]
   Thus these three neighborhoods in \(C\) have sizes \(4,5,6\).

6. For \(1\le i\le6\), join \(u_i\) to \(b_j\) precisely when
   \[
   i+j\ge7.
   \]
   Also put the edges
   \[
   u_1c_4,\quad u_2c_5,\quad u_3c_5,\quad
   u_4c_6,\quad u_5c_6,\quad u_6c_6.
   \]

In particular, \(T\cup U\) is independent, and \(z\) is isolated.

### 2. Verification

#### Degrees

The complete degree table is
\[
\begin{array}{c|c|c}
\text{Vertices}&\text{Degree}&\text{Number of vertices}\\ \hline
z&0&1\\
u_i,\ 1\le i\le12&i&12\\
a_1,a_2,t_1,\ldots,t_6&13&8\\
a_3,a_4,a_5&14,15,16&3\\
c_j,\ 0\le j\le6&17+j&7\\
b_j,\ 0\le j\le5&24+j&6
\end{array}
\]

Here are direct checks of the less immediate entries.

- Each \(a_i\) has \(13\) neighbors in \(B\cup C\), and the extra degrees supplied by \(U\) are \(0,0,1,2,3\).
- Each \(b_j\) has \(12\) neighbors in \(A\cup C\), six in \(T\), six among \(u_7,\ldots,u_{12}\), and exactly \(j\) among \(u_1,\ldots,u_6\). Thus
  \[
  d(b_j)=12+6+6+j=24+j.
  \]
- Each \(c_j\) has \(11\) neighbors in \(A\cup B\), six in \(T\), and exactly \(j\) in \(U\). Hence
  \[
  d(c_j)=17+j.
  \]
- For \(1\le i\le6\), the vertex \(u_i\) has \(i-1\) neighbors in \(B\) and one in \(C\). The definitions likewise give \(d(u_i)=i\) for \(7\le i\le12\).

Consequently,
\[
\{d(v):v\in V(G)\}=\{0,1,\ldots,29\},
\]
so
\[
w(G)=30.
\]

#### Chromatic number

The following are three independent sets partitioning \(V(G)\):
\begin{equation*}
\begin{aligned}
I_1&=A\cup T\cup\{u_1,\ldots,u_6,u_{10},u_{11},u_{12},z\},\\
I_2&=B,\\
I_3&=C\cup\{u_7,u_8,u_9\}.
\end{aligned}
\end{equation*}
Therefore \(\chi(G)\le3\). Since \(a_1b_0c_0a_1\) is a triangle,
\[
\chi(G)=3.
\]

#### Failure of the proposed inequality

For this graph,
\[
|V(G)|-w(G)=37-30=7
\]
and
\[
\left\lceil
\frac{\lfloor w(G)/2\rfloor}{|V(G)|-w(G)}
\right\rceil
=
\left\lceil\frac{15}{7}\right\rceil
=3.
\]
Thus the proposed conclusion is \(3>3\), which is false.

The graph has exactly one isolated vertex; its other \(36\) vertices form a connected component.

---

## 3. Minimality: no counterexample has fewer than 37 vertices

The following argument is not needed for the disproof, but establishes that the order of the construction is optimal.

Write
\[
n=|V(G)|,\qquad k=\chi(G),\qquad t=n-w(G).
\]
For a simple graph on at least two vertices, \(w(G)\le n-1\), so \(t\ge1\).

The proposed inequality is equivalent to
\[
\left\lfloor\frac{w(G)}2\right\rfloor\le(k-1)t,
\]
and hence to
\[
\boxed{n\le(2k-1)t+1.} \qquad\text{(1)}
\]

We prove two facts:

1. every bipartite graph satisfies (1);
2. every graph with \(t\le6\) satisfies (1).

These imply minimality immediately. Indeed, a counterexample has \(k\ge3\) and
\[
n\ge(2k-1)t+2\ge5t+2.
\]
If \(n\le36\), this forces \(t\le6\), contradicting the second fact.

### 3.1 Bipartite graphs

First suppose the graph has no isolated vertices. Take a bipartition with part sizes \(a\le b\).

All degrees lie in \(\{1,\ldots,b\}\), giving \(w\le b\). The larger part contributes at most \(a\) degree values, and the smaller part has only \(a\) vertices, so \(w\le2a\). Therefore
\[
n=a+b\ge \frac w2+w,
\]
or equivalently
\[
n\le3(n-w)=3t. \qquad\text{(2)}
\]

If a nonempty graph has \(r\ge1\) isolated vertices, deleting all of them gives a graph \(G_0\) with
\[
n_0=n-r,\qquad w_0=w-1,\qquad t_0=t-r+1.
\]
Applying (2),
\[
n=n_0+r\le3t_0+r=3t-2r+3\le3t+1.
\]
Edgeless graphs satisfy the original inequality directly. Thus every bipartite graph satisfies (1).

### 3.2 A degree-spread estimate

Consider a graph of even order \(2m\), with its degrees arranged as
\[
d_1\le\cdots\le d_{2m}.
\]
Let \(L\) be the first \(m\) vertices and \(H\) the last \(m\). Put
\[
b=d_m,\qquad \delta=d_1,\qquad
D=\sum_{v\in H}d(v)-\sum_{v\in L}d(v).
\]
Then
\[
D=\sum_{i=1}^{2m}|d_i-b|
   =2e(H)-2e(L). \qquad\text{(3)}
\]
In particular, \(D\) is even.

If there are \(w\) distinct degrees, selecting one occurrence of each degree in the absolute-value sum gives
\[
D\ge D_0:=\left\lfloor\frac{w^2}{4}\right\rfloor. \qquad\text{(4)}
\]
Indeed, the minimum sum of distances from an integer \(b\) to \(w\) distinct integers is \(\lfloor w^2/4\rfloor\).

We also need the following refinements, using that every degree is at least \(\delta\):

- If \(w=2r+1\) and \(b\le\delta+r\), then
  \[
  D\ge r(r+1)+(\delta+r-b)^2. \qquad\text{(5)}
  \]
- If \(w=2r\) and \(b\le\delta+r-1\), then
  \[
  D\ge r^2+(\delta+r-1-b)(\delta+r-b). \qquad\text{(6)}
  \]

For completeness, under the hypothesis of (5), the \(2r+1\) closest distinct integers at least \(\delta\) are
\[
\delta,\delta+1,\ldots,\delta+2r.
\]
Their distances from \(b\) sum to the right-hand side of (5). The same argument with
\(\delta,\ldots,\delta+2r-1\) proves (6).

### 3.3 Incorporating a coloring

Fix a proper \(k\)-coloring and let \(h_i\) be the number of vertices of color \(i\) in \(H\). Set
\[
a=\min_i h_i,\qquad e=e(L).
\]
Since there are no edges within a color class,
\[
D+2e+\sum_{i=1}^k h_i^2\le m^2. \qquad\text{(7)}
\]
Also, any vertex of \(L\) has at most \(m-a\) neighbors in \(H\), and at most \(e\) neighbors in \(L\). Hence
\[
b\le m-a+e. \qquad\text{(8)}
\]

Let
\[
Q_k(m)=
\min\left\{\sum_{i=1}^k x_i^2:
x_i\in\mathbb Z_{\ge0},\ \sum_i x_i=m\right\}.
\]
The minimum occurs when the \(x_i\)'s differ by at most one. This follows by transferring one unit from a larger entry to a smaller entry whenever they differ by at least two.

Since \(w=2m-t\),
\[
D_0=m^2-tm+\left\lfloor\frac{t^2}{4}\right\rfloor.
\]
Equations (4) and (7), together with Cauchy–Schwarz, give
\[
\frac{m^2}{k}\le Q_k(m)
\le tm-\left\lfloor\frac{t^2}{4}\right\rfloor. \qquad\text{(9)}
\]

For \(k\ge2\), the quadratic inequality (9) yields
\[
\begin{array}{c|c}
t&\text{Upper bound on }m\\ \hline
1&k\\
2&2k-1\\
3&3k-1\\
4&4k-2\\
5&5k-2\\
6&6k-2
\end{array} \qquad\text{(10)}
\]
For example, at one more than these bounds, the left side minus the right side of (9) is respectively
\[
1+\frac1k,\quad 1,\quad 2,\quad
\frac1k,\quad 1+\frac1k,\quad 3+\frac1k,
\]
and the quadratic is increasing thereafter.

Only four boundary cases need refinement. Define
\[
X=D-D_0,\qquad
E=\sum_i h_i^2-Q_k(m).
\]
Both are nonnegative integers, and \(E\) is even, because \(x^2\equiv x\pmod2\). From (7),
\[
X+2e+E\le m^2-D_0-Q_k(m). \qquad\text{(11)}
\]

The relevant boundary data are
\[
\begin{array}{c|c|c|c|c}
t&m&Q_k(m)&m^2-D_0-Q_k(m)&a\text{ when }E=0\\ \hline
1&k&k&0&1\\
3&3k-1&9k-5&0&2\\
5&5k-2&25k-18&2&4\\
6&6k-2&36k-22&1&5
\end{array} \qquad\text{(12)}
\]

#### The boundaries \(t=1,3\)

Assume there are no isolated vertices, so \(\delta\ge1\).

Equation (11) forces \(X=e=E=0\). For \(t=1\), write \(w=2r+1\) with \(r=m-1\); for \(t=3\), use \(r=m-2\). In both cases, (8) and (12) give \(b\le r\). But (5), with \(X=0\), requires
\[
b\ge\delta+r\ge r+1,
\]
a contradiction.

Thus these boundary orders cannot occur without isolated vertices.

#### The boundary \(t=5\)

Again assume \(\delta\ge1\). Here
\[
m=5k-2,\qquad w=2r+1,\qquad r=m-3,
\]
and
\[
X+2e+E\le2.
\]
Since \(D_0=r(r+1)\) and \(D\) are even, \(X\) is even.

We use the observation that \(E\le2\) forces \(a\ge3\). Otherwise, some \(h_i\le2\); because their sum is \(5k-2\), another entry is at least \(6\). Transferring one unit between these entries decreases the sum of squares by at least \(6\), implying \(E\ge6\), a contradiction.

If \(X=0\), there are two possibilities:

- \(E=0\), so \(a=4\) and \(e\le1\);
- \(E=2\), so \(e=0\) and \(a\ge3\).

In either case, (8) gives \(b\le m-3\). But (5), with \(X=0\), requires
\[
b\ge\delta+r\ge m-2.
\]

If \(X=2\), then \(e=E=0\), so \(a=4\) and \(b\le m-4\). Hence
\[
\delta+r-b\ge2,
\]
and (5) gives \(X\ge4\), again a contradiction.

Thus this boundary also cannot occur without isolated vertices.

#### The boundary \(t=6\)

Here no assumption about isolated vertices is needed. We have
\[
m=6k-2,\qquad w=2r,\qquad r=m-3=6k-5.
\]
Thus \(D_0=r^2\) is odd. Since \(D\) is even, \(X\) is a positive odd integer. Equation (11) therefore forces
\[
X=1,\qquad e=E=0.
\]
By (12), \(a=5\), and consequently
\[
b\le m-5=r-2.
\]
As \(\delta\ge0\), inequality (6) gives
\[
D\ge r^2+2,
\]
contradicting \(X=1\).

This boundary is impossible for every graph.

### 3.4 Completion for \(t\le6\)

The preceding estimates show that for every even-order nonempty graph with \(t\le6\),
\[
n\le
\begin{cases}
(2k-1)t,&t\text{ even},\\
(2k-1)t+1,&t\text{ odd},
\end{cases} \qquad\text{(13)}
\]
and in the odd-\(t\) case equality in (13) requires an isolated vertex.

It follows that every graph **without isolated vertices** and with \(t\le6\) satisfies
\[
n\le(2k-1)t. \qquad\text{(14)}
\]
For even order this is already proved. For odd order, add one isolated vertex. This increases both \(n\) and \(w\) by one, leaving \(t\) and \(k\) unchanged. Applying (13) to the resulting even-order graph gives (14).

Finally, suppose a nonempty graph has \(r\ge1\) isolated vertices. Deleting them gives
\[
t_0=t-r+1\le6.
\]
Applying (14) to the remaining graph,
\begin{equation*}
\begin{aligned}
n
&\le (2k-1)t_0+r\\
&=(2k-1)t-(2k-2)r+(2k-1)\\
&\le(2k-1)t+1.
\end{aligned}
\end{equation*}
Edgeless graphs satisfy the original assertion directly. Therefore every graph with \(t\le6\) satisfies (1).

As explained above, this excludes every counterexample on at most \(36\) vertices. The constructed \(37\)-vertex graph is therefore smallest possible.

---

### Conclusion and scope

The displayed conjecture is **false as stated**, and the minimum counterexample order is \(37\).

The isolated vertex is material: deleting it from the construction leaves a graph that satisfies the displayed inequality. Thus the construction does not by itself refute a version restricted to connected graphs. No computational search or unverified literature result is used in the argument; whether this counterexample or its minimality has previously appeared remains a bibliographic question.
