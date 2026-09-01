```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the standard ordinary-critical (equivalently fixed constant-list-critical) interpretation, the optimal guaranteed sparsity is exactly zero whenever 0<alpha<2epsilon<1.",
  "would_publish": false,
  "caveats": "The boundary alpha=2epsilon and the main positive regime alpha>2epsilon remain open; choice-criticality in the stronger list-chromatic-number sense is not covered."
}
```

## 1. Setup

Write \(D=\Delta(G)\). I use the standard definition from the sparse-neighborhood literature:

\[
G\text{ is }\delta\text{-sparse}\quad\Longleftrightarrow\quad
e(G[N(v)])\le (1-\delta)\binom D2
\quad\text{for every }v\in V(G).
\]

The argument is unchanged if \(\binom{d(v)}2\) is used instead, because the witnessing vertices below are universal.

Let \(\delta^*(\varepsilon,\alpha)\) denote the largest universally valid \(\delta\), equivalently the infimum, over all qualifying graphs, of

\[
\min_{v\in V(G)}
\frac{\binom D2-e(G[N(v)])}{\binom D2}.
\]

The source paper's established King–Reed-type lower bound in the positive regime is

\[
\delta^*(\varepsilon,\alpha)\ge
\frac12(\alpha-2\varepsilon)^2
\qquad(\alpha>2\varepsilon),
\]

up to the harmless conventions associated with rounding. The result below shows that the threshold \(\alpha=2\varepsilon\) is genuine: below it, no positive sparsity constant is possible.

---

## 2. Main partial result

### Theorem

Let

\[
0<\varepsilon<\frac12,\qquad 0\le \alpha<2\varepsilon.
\]

For every \(\delta>0\), there are arbitrarily large graphs \(G\) such that

\[
\chi(G)=\lfloor(1-\varepsilon)(\Delta(G)+1)\rfloor+1,
\]

\(G\) is critical,

\[
\omega(G)\le (1-\alpha)(\Delta(G)+1),
\]

but \(G\) is not \(\delta\)-sparse. Consequently,

\[
\boxed{\delta^*(\varepsilon,\alpha)=0
\quad\text{for }0\le\alpha<2\varepsilon<1.}
\]

The graphs are also critical for the constant list assignment with
\(\chi(G)-1\) colors.

The proof uses dense critical building blocks asymptotically attaining the elementary inequality

\[
\chi(X)\le \frac{|X|+\omega(X)}2.
\]

---

## 3. A Ramsey-type building block

We first need critical graphs \(H\) for which

\[
\frac{|H|-\omega(H)}{|H|-\chi(H)}
\]

is arbitrarily close to \(2\).

### Lemma 1

For every \(\eta>0\), there are arbitrarily large odd integers \(h\) and an \(r\)-critical graph \(H\) on \(h\) vertices such that

\[
r=\frac{h+1}{2}
\qquad\text{and}\qquad
\omega(H)\le \eta h.
\]

#### Proof

We first construct an odd-order triangle-free Hamiltonian graph \(F\) with independence number at most \(\eta h\).

Fix \(0<\gamma<\eta/2\). Choose an integer \(q_0\) so large that

\[
q_0\gamma^2>H(\gamma),
\]

where \(H(x)=-x\log x-(1-x)\log(1-x)\) is binary entropy. For an arbitrarily large odd \(h\), take \(q_0\) independent uniformly random Hamilton cycles
\(C_1,\dots,C_{q_0}\) on a common \(h\)-vertex set, and let \(U\) be their union.

For a fixed set \(S\) of \(s\le h/2\) vertices, the probability that \(S\) is independent in one random Hamilton cycle is

\[
p_{h,s}
=
\frac{h}{h-s}
\frac{\binom{h-s}{s}}{\binom hs}.
\]

Indeed, this is the proportion of \(s\)-subsets of cyclic positions containing no two consecutive positions. Moreover,

\[
p_{h,s}
\le
\frac{h}{h-s}\exp\left(-\frac{s^2}{h}\right).
\]

Taking \(s=\lceil\gamma h\rceil\), a union bound therefore gives

\[
\Pr(\alpha_{\rm ind}(U)\ge s)
\le
\binom hs p_{h,s}^{q_0}
=
\exp\!\left(
h\bigl(H(\gamma)-q_0\gamma^2+o(1)\bigr)
\right)
=o(1).
\]

The expected number of triangles in \(U\) is \(O(q_0^3)\). To see this, fix three vertices and assign each of the three potential triangle edges to one of the \(q_0\) cycles witnessing that edge. A fixed edge belongs to a random Hamilton cycle with probability \(2/(h-1)\), while two prescribed adjacent edges both belong to it with probability \(2/((h-1)(h-2))\). Summing over the \(q_0^3\) assignments gives probability \(O(q_0^3h^{-3})\) for a fixed triple, and hence \(O(q_0^3)\) expected triangles in total. Thus the number of triangles is \(o(h)\) with probability tending to one.

Choose an outcome for which

\[
\alpha_{\rm ind}(U)<\gamma h
\quad\text{and}\quad
T(U)<\gamma h.
\]

For each triangle of \(U\), delete one edge not belonging to \(C_1\). Such an edge exists because \(C_1\) itself contains no triangle. Let the resulting graph be \(F\). Then:

* \(F\) is triangle-free;
* \(F\) still contains the Hamilton cycle \(C_1\);
* at most \(T(U)<\gamma h\) edges were deleted.

Deleting \(t\) edges can increase the independence number by at most \(t\): from an independent set in the graph after deletion, remove at most one endpoint for each restored edge. Hence

\[
\alpha_{\rm ind}(F)
\le \alpha_{\rm ind}(U)+T(U)
<2\gamma h
<\eta h.
\]

Now consider \(\overline F\). Since \(F\) is triangle-free, every independent set in \(\overline F\) has size at most two. Since \(F\) has an odd Hamilton cycle, it has a matching of size \((h-1)/2\). Therefore

\[
\chi(\overline F)=\frac{h+1}{2}.
\]

Moreover, deleting any vertex from the Hamilton cycle leaves a path with a perfect matching. Thus for every vertex \(v\),

\[
\chi(\overline F-v)=\frac{h-1}{2}.
\]

Choose a spanning subgraph \(H\subseteq\overline F\), edge-minimal subject to

\[
\chi(H)=\frac{h+1}{2}.
\]

Then deleting any edge of \(H\) lowers its chromatic number, while deleting any vertex gives a subgraph of \(\overline F-v\), which is \((h-1)/2\)-colorable. Thus \(H\) is \(r\)-critical for

\[
r=\frac{h+1}{2}.
\]

Finally,

\[
\omega(H)\le\omega(\overline F)
=\alpha_{\rm ind}(F)
<\eta h.
\]

This proves the lemma. \(\square\)

Define for such an \(H\)

\[
a:=h-\chi(H)=\frac{h-1}{2},
\qquad
b:=h-\omega(H).
\]

Then

\[
\frac{b}{a}
\ge
\frac{2(1-\eta)h}{h-1},
\]

so \(b/a\) can be made arbitrarily close to \(2\) from below. Also \(a/h\) can be made arbitrarily close to \(1/2\).

---

## 4. Joining the building blocks

We use the complete join \(A\vee B\), obtained by adding every edge between \(A\) and \(B\).

### Lemma 2

If \(A\) is \(p\)-critical and \(B\) is \(q\)-critical, then \(A\vee B\) is \((p+q)\)-critical.

#### Proof

Certainly

\[
\chi(A\vee B)=\chi(A)+\chi(B)=p+q.
\]

Deleting a vertex or an internal edge from one factor permits a \((p+q-1)\)-coloring by using disjoint palettes on the two factors.

If a cross-edge \(xy\), with \(x\in A\) and \(y\in B\), is deleted, color \(A-x\) with \(p-1\) colors and \(B-y\) with \(q-1\) disjoint colors, and give \(x\) and \(y\) one common new color. This uses \(p+q-1\) colors. Thus every proper subgraph is \((p+q-1)\)-colorable. \(\square\)

---

## 5. Proof of the theorem

Fix \(0<\varepsilon<1/2\) and \(0\le\alpha<2\varepsilon\). Choose \(\eta>0\) sufficiently small that

\[
2(1-\eta)>\frac{\alpha}{\varepsilon}.
\]

Using Lemma 1, choose \(h\) large enough that the resulting critical graph \(H\) satisfies both

\[
\frac{a}{h}=\frac{h-1}{2h}>\varepsilon
\]

and

\[
\frac{b}{a}>\frac{\alpha}{\varepsilon}.
\]

For every positive integer \(m\), set

\[
N_m:=\left\lfloor\frac{ma}{\varepsilon}\right\rfloor+1
\]

and

\[
t_m:=N_m-mh.
\]

Since \(a/h>\varepsilon\),

\[
t_m
=
m\left(\frac{a}{\varepsilon}-h\right)+O(1)>0
\]

for all sufficiently large \(m\). Define

\[
G_m:=K_{t_m}\vee
\underbrace{H\vee\cdots\vee H}_{m\text{ copies}}.
\]

By Lemma 2, \(G_m\) is critical. Its order is \(N_m\), and the clique factor \(K_{t_m}\) supplies universal vertices, so

\[
\Delta(G_m)+1=N_m.
\]

Also,

\[
\chi(G_m)
=t_m+m(h-a)
=N_m-ma.
\]

By the definition of \(N_m\),

\[
ma<\varepsilon N_m<ma+1.
\]

Consequently,

\[
\lceil\varepsilon N_m\rceil=ma+1,
\]

and hence

\[
\begin{aligned}
\lfloor(1-\varepsilon)N_m\rfloor+1
&=N_m-\lceil\varepsilon N_m\rceil+1\\
&=N_m-ma\\
&=\chi(G_m).
\end{aligned}
\]

Thus the criticality index is exactly the one in the question, including the floor.

The clique number is

\[
\omega(G_m)
=t_m+m\omega(H)
=N_m-mb.
\]

Since \(N_m/m\to a/\varepsilon\),

\[
\frac{mb}{N_m}\longrightarrow
\frac{b\varepsilon}{a}>\alpha.
\]

Therefore, for all sufficiently large \(m\),

\[
\omega(G_m)=N_m-mb
\le(1-\alpha)N_m
=(1-\alpha)(\Delta(G_m)+1).
\]

It remains to examine neighborhood sparsity. Let \(x\) be any vertex of the clique \(K_{t_m}\). Then \(x\) is universal, and all nonedges in \(G_m[N(x)]\) lie inside individual copies of \(H\). If

\[
M_H:=\binom h2-e(H),
\]

then

\[
\binom{\Delta(G_m)}2-e(G_m[N(x)])
=mM_H.
\]

On the other hand, \(N_m=\Theta(m)\), so

\[
\frac{mM_H}{\binom{N_m-1}{2}}
\longrightarrow 0.
\]

Given any fixed \(\delta>0\), sufficiently large \(m\) therefore satisfies

\[
e(G_m[N(x)])
>
(1-\delta)\binom{\Delta(G_m)}2.
\]

Thus \(G_m\) is not \(\delta\)-sparse. Since every graph is \(0\)-sparse, the optimal universal guarantee is exactly zero. \(\square\)

---

## 6. Why the threshold \(2\varepsilon\) appears

The construction asymptotically saturates an elementary obstruction for critical graphs having a universal vertex.

For every graph \(X\) on \(n\) vertices,

\[
\chi(X)\le\frac{n+\omega(X)}2.
\]

Indeed, take a maximal matching in \(\overline X\). Its unmatched vertices form a clique in \(X\); color each matched nonedge-pair with one color and each unmatched vertex separately.

Now suppose a \(k\)-critical graph \(G\) has a universal vertex \(v\), and let \(n=\Delta(G)+1=|G|\). Then

\[
\chi(G-v)=k-1,\qquad
\omega(G-v)=\omega(G)-1.
\]

Applying the preceding inequality to \(G-v\) gives

\[
k-1
\le
\frac{(n-1)+(\omega(G)-1)}2,
\]

or

\[
n-\omega(G)\le2(n-k).
\]

For the criticality index in the question,

\[
n-k=\lceil\varepsilon n\rceil-1<\varepsilon n.
\]

Hence every such universal-vertex example necessarily has

\[
n-\omega(G)<2\varepsilon n.
\]

Thus it can only meet the clique hypothesis when \(\alpha<2\varepsilon\). Lemma 1 shows that this elementary inequality is asymptotically sharp even among critical graphs, which is exactly why the construction covers the entire strict range \(\alpha<2\varepsilon\).

At \(\alpha=2\varepsilon\), no universal-vertex example can work because of the strict rounding inequality above. The boundary could therefore behave differently.

---

## 7. An explicit boundary benchmark

The boundary is not settled, but there is a useful exact family at one point.

Let \(s\ge3\) be odd, let

\[
F_s=C_5[\overline{K_s}]
\]

be the balanced independent-set blow-up of \(C_5\), and put \(J_s=\overline{F_s}\). Then:

\[
|J_s|=5s,\qquad
\Delta(J_s)=3s-1,
\]

\[
\chi(J_s)=\frac{5s+1}{2},
\qquad
\omega(J_s)=2s.
\]

Moreover, \(J_s\) is critical. Vertex deletion leaves a perfect matching in \(F_s\). If an edge of \(J_s\) is deleted, its endpoints either lie in the same blow-up part or in two distance-two parts of the \(C_5\); in either case they have a common neighbor in \(F_s\). These three vertices form one color class after the edge deletion, and the remaining vertices have a perfect matching in \(F_s\), yielding a \((\chi(J_s)-1)\)-coloring.

For

\[
\varepsilon=\frac16,\qquad \alpha=\frac13=2\varepsilon,
\]

we have

\[
\left\lfloor
\left(1-\frac16\right)(\Delta(J_s)+1)
\right\rfloor+1
=
\left\lfloor\frac{5s}{2}\right\rfloor+1
=
\frac{5s+1}{2},
\]

and

\[
\omega(J_s)=2s
=
\left(1-\frac13\right)(\Delta(J_s)+1).
\]

For a vertex in one blow-up part, its \(J_s\)-neighborhood consists of its own part minus that vertex and the two distance-two parts. Exactly \(s^2\) pairs in this neighborhood are nonedges. Therefore its missing-edge proportion is

\[
\frac{s^2}{\binom{3s-1}{2}}
\longrightarrow \frac29.
\]

Consequently,

\[
\delta^*\!\left(\frac16,\frac13\right)\le\frac29.
\]

The known general lower bound gives only zero at this boundary point, so the interval

\[
0\le
\delta^*\!\left(\frac16,\frac13\right)
\le\frac29
\]

remains open.

---

## 8. What remains unresolved

The construction completely settles the strict zero-sparsity region

\[
\alpha<2\varepsilon,\qquad \varepsilon<\frac12.
\]

It does not determine:

1. the boundary \(\alpha=2\varepsilon\);
2. the optimal positive value for \(\alpha>2\varepsilon\);
3. the stronger interpretation in which “\(k\)-list-critical” means critical with respect to the list-chromatic number itself, rather than \(L\)-critical for some fixed \((k-1)\)-list assignment.

Under the ordinary or fixed-list-critical interpretation, the remaining central gap is therefore between the established quadratic lower bound in \(\alpha-2\varepsilon\) and any sharp upper constructions in the positive regime.