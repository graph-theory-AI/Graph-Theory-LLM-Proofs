```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The optimal coefficient is at least linear in |V(H)| for every H, and it is Θ(|V(H)|) for every tree H—indeed exactly determined for linear forests—but the general planar case remains open.",
  "would_publish": false,
  "caveats": "The upper bounds cover trees, linear forests, and bounded packing number for connected planar H; they do not give a polynomial coefficient for arbitrary planar H and unbounded k."
}
```

# Mathematical writeup

## 1. Notation and results obtained

For a graph \(H\), write

\[
\nu_H(G)=\max\{r:\text{\(G\) contains \(r\) vertex-disjoint \(H\)-models}\}
\]

and

\[
\tau_H(G)=\min\{|X|:G-X\text{ is \(H\)-minor-free}\}.
\]

Fix a base for the logarithm and define the optimal coefficient

\[
c_*(H):=
\sup_{\substack{G,\ k\ge 1\\ \nu_H(G)<k}}
\frac{\tau_H(G)}{k\log(k+1)}.
\]

The theorem in the source paper says that \(c_*(H)<\infty\) for every planar \(H\).

Let \(h=|V(H)|\). The following partial results hold.

### Partial theorem

1. For every nonempty graph \(H\),
   \[
   c_*(H)\ge \alpha_{\log}\,h,
   \qquad
   \alpha_{\log}:=
   \sup_{k\ge2}\frac{k-1}{k\log(k+1)}.
   \]
   Thus any affirmative polynomial upper bound must have degree at least one.

2. If \(H\) is a linear forest, then equality holds:
   \[
   c_*(H)=\alpha_{\log}\,h.
   \]
   For natural logarithms,
   \[
   \alpha_{\log}=\frac{2}{3\log 4}=\frac1{3\log 2};
   \]
   for logarithms to base \(2\), \(\alpha_{\log}=1/3\).

3. If \(T\) is any tree on \(h\) vertices and \(r=\nu_T(G)\), then
   \[
   \tau_T(G)
   \le
   2hr\bigl(\lfloor\log_2 r\rfloor+1\bigr)
   \quad (r\ge1).
   \]
   Consequently,
   \[
   c_*(T)=\Theta(h),
   \]
   with absolute implied constants. In particular, the desired polynomial dependence holds, optimally up to an absolute factor, for every tree pattern.

4. For every connected planar \(H\), graphs with \(\nu_H(G)\le1\) have an \(H\)-transversal of size polynomial in \(h\). More generally, for fixed packing number \(r\), \(\tau_H(G)\) is polynomial in \(h\) and \(r\). Thus a possible superpolynomial dependence cannot already be forced at \(k=2\) for connected planar patterns.

The proofs follow.

---

## 2. A universal linear lower bound

Let \(k\ge2\) and take

\[
G=K_{hk-1}.
\]

Every graph containing \(H\) as a minor has at least \(h\) vertices, since minor operations do not increase the number of vertices. Therefore

\[
\nu_H(G)\le \left\lfloor\frac{hk-1}{h}\right\rfloor=k-1.
\]

Conversely, each set of \(h\) vertices in \(G\) contains \(H\) as a subgraph after deleting unwanted edges. Hence equality holds:

\[
\nu_H(G)=k-1.
\]

Moreover, \(K_m\) is \(H\)-minor-free exactly when \(m<h\). Thus every \(H\)-transversal of \(G\) has size at least

\[
(hk-1)-(h-1)=h(k-1),
\]

and deleting that many vertices is sufficient. Hence

\[
\tau_H(K_{hk-1})=h(k-1).
\]

It follows that

\[
c_*(H)\ge
h\frac{k-1}{k\log(k+1)}
\]

for every \(k\ge2\), proving

\[
c_*(H)\ge \alpha_{\log}h.
\]

For natural logarithms, the function

\[
x\longmapsto\frac{x-1}{x\log(x+1)}
\]

is decreasing for \(x\ge3\), and its value at \(3\) exceeds its value at \(2\). Thus the discrete maximum occurs at \(k=3\), giving

\[
\alpha_{\log}=\frac{2}{3\log4}=\frac1{3\log2}.
\]

This lower bound applies to every \(H\), planar or not.

---

## 3. Exact answer for linear forests

Suppose that \(H\) is a disjoint union of paths, with \(h\) vertices in total.

### Lemma 3.1

If a graph contains a linear forest \(H\) as a minor, then it contains \(H\) as a subgraph.

#### Proof

It suffices to consider one component \(P_\ell\). Given a \(P_\ell\)-minor model with branch sets \(B_1,\dots,B_\ell\), choose the model edges between consecutive branch sets and, within each internal branch set, a path joining its two attachment vertices. Their union contains a simple path meeting the branch sets in order, and hence a path with at least \(\ell\) vertices. It contains \(P_\ell\) as a subgraph.

Applying this separately to the mutually disjoint branch sets corresponding to the components of \(H\) gives a copy of the whole linear forest. ∎

Let \(r=\nu_H(G)\), and take a maximum collection of \(r\) vertex-disjoint copies of \(H\). Their union \(X\) has exactly \(hr\) vertices. If \(G-X\) contained an \(H\)-minor, Lemma 3.1 would give an additional copy of \(H\), contrary to maximality. Therefore

\[
\tau_H(G)\le h\nu_H(G).
\]

If \(\nu_H(G)<k\), this yields

\[
\tau_H(G)\le h(k-1).
\]

Consequently,

\[
c_*(H)\le
h\sup_{k\ge2}\frac{k-1}{k\log(k+1)}
=\alpha_{\log}h.
\]

Together with the complete-graph construction, this proves the exact formula

\[
\boxed{c_*(H)=\alpha_{\log}|V(H)|}
\]

for every linear forest \(H\).

---

## 4. A separator lemma

The tree case uses the following general mechanism.

### Lemma 4.1

Let \(H\) be connected. Suppose there is a constant \(a\) such that every graph \(J\), with \(s=\nu_H(J)\), satisfies

\[
\operatorname{tw}(J)+1\le a(s+1).
\tag{4.1}
\]

Then, for \(r=\nu_H(G)\ge1\),

\[
\tau_H(G)
\le
2ar\bigl(\lfloor\log_2r\rfloor+1\bigr).
\tag{4.2}
\]

#### Proof

We first record a balanced-bag fact. Let \((D,\{B_t:t\in V(D)\})\) be a tree decomposition of \(J\). For an edge \(xy\in E(D)\), deleting \(xy\) divides \(D\) into two sides. After removing the adhesion \(B_x\cap B_y\), the corresponding vertex sets in \(J\) are disjoint and have no edges between them.

Orient \(xy\) toward a side if that side contains more than \(s/2\) vertex-disjoint \(H\)-models. Both orientations cannot occur, since the two packings could then be combined to give more than \(s\) disjoint models. Likewise, at any decomposition node, at most one incident edge can point away from that node. Following outgoing edges therefore terminates at a node \(t\) with no outgoing edge.

Every component \(C\) of \(J-B_t\) is represented entirely in one branch of \(D-t\). By the choice of \(t\),

\[
\nu_H(C)\le s/2.
\tag{4.3}
\]

By (4.1), \(J\) has a tree decomposition with a bag \(B_t\) satisfying

\[
|B_t|\le a(s+1)\le 2as
\quad (s\ge1).
\]

Delete \(B_t\) and recurse on every component \(C\) of \(J-B_t\) with positive \(H\)-packing number. Since \(H\) is connected, every \(H\)-model avoiding \(B_t\) lies wholly in one such component.

Consider the resulting recursion tree. A node labelled \(s'\) incurs cost at most \(2as'\); its children have labels at most \(s'/2\), and the sum of the child labels is at most \(s'\), because the corresponding components are vertex-disjoint. Hence the sum of labels at every recursion depth is at most \(r\), so each depth costs at most \(2ar\). Along every branch the label is halved, giving at most

\[
\lfloor\log_2r\rfloor+1
\]

nonempty levels. This proves (4.2). ∎

---

## 5. Application to every tree \(T\)

We use the established forest–pathwidth theorem:

> If \(F\) is a forest on \(N\) vertices and \(\operatorname{pw}(J)\ge N-1\), then \(J\) contains \(F\) as a minor.

Let \(T\) be a tree on \(h\) vertices, and put \(s=\nu_T(J)\). Let \(F\) be the disjoint union of \(s+1\) copies of \(T\), so that

\[
|V(F)|=h(s+1).
\]

If

\[
\operatorname{pw}(J)\ge h(s+1)-1,
\]

then \(J\) contains \(F\) as a minor. Splitting the model according to the components of \(F\) would give \(s+1\) vertex-disjoint \(T\)-models, contradicting the definition of \(s\). Therefore

\[
\operatorname{tw}(J)+1
\le
\operatorname{pw}(J)+1
\le h(s+1).
\]

Thus Lemma 4.1 applies with \(a=h\), yielding

\[
\boxed{
\tau_T(G)
\le
2h\nu_T(G)
\bigl(\lfloor\log_2\nu_T(G)\rfloor+1\bigr).
}
\]

If \(\nu_T(G)<k\), then, for \(k\ge2\),

\[
\tau_T(G)
\le
4hk\log_2(k+1).
\]

Thus one can take \(c(T)\le4h\) when the logarithm is base \(2\); changing the logarithm base only changes the absolute constant. Combining this with the universal complete-graph lower bound gives

\[
\boxed{c_*(T)=\Theta(|V(T)|)}
\]

uniformly over all trees \(T\).

---

## 6. Polynomial dependence when the packing number is bounded

This section applies to an arbitrary connected planar \(H\).

### Lemma 6.1

If \(H\) is connected and \(G\) has treewidth \(w\), then

\[
\tau_H(G)\le (w+1)\nu_H(G).
\tag{6.1}
\]

#### Proof

Take a width-\(w\) tree decomposition with decomposition tree \(D\). For every connected \(H\)-model \(M\), let \(D_M\) be the set of decomposition nodes whose bags meet \(M\). Since \(M\) is connected, \(D_M\) is a subtree of \(D\).

For a finite family of subtrees of a tree, the minimum number of tree nodes meeting every subtree equals the maximum number of pairwise node-disjoint subtrees. If \(D_{M_1},\dots,D_{M_q}\) are node-disjoint, then \(M_1,\dots,M_q\) are vertex-disjoint: a common graph vertex would occur in a bag belonging to both traces. Hence \(q\le\nu_H(G)\).

There are therefore at most \(\nu_H(G)\) decomposition nodes whose bags meet every \(H\)-model. The union of these bags is an \(H\)-transversal of size at most \((w+1)\nu_H(G)\). ∎

Let \(Q_q\) denote the \(q\times q\) grid. Define

\[
q(H)=\min\{q:H\preceq Q_q\},
\]

and let \(\gamma(q)\) be a threshold such that every graph of treewidth at least \(\gamma(q)\) contains \(Q_q\) as a minor.

The established polynomial excluded-grid theorem gives universal constants \(A,d\) such that

\[
\gamma(q)\le Aq^d.
\tag{6.2}
\]

Also, standard polynomial-area planar grid drawings imply

\[
q(H)\le h^{O(1)}.
\tag{6.3}
\]

For completeness, one can obtain (6.3) by replacing every high-degree vertex of \(H\) by a planar subcubic tree of ports, producing a subcubic planar graph of \(O(h)\) vertices that contracts to \(H\), and then using a polynomial-area orthogonal grid drawing of that graph.

Now put \(r=\nu_H(G)\) and

\[
q=q(H)\left\lceil\sqrt{r+1}\right\rceil.
\]

A \(q\times q\) grid contains at least \(r+1\) vertex-disjoint \(q(H)\times q(H)\) subgrids. Hence, if

\[
\operatorname{tw}(G)\ge\gamma(q),
\]

then \(G\) contains \(r+1\) vertex-disjoint \(H\)-models, a contradiction. Thus

\[
\operatorname{tw}(G)<\gamma(q).
\]

Lemma 6.1 gives

\[
\boxed{
\tau_H(G)
\le
r\,\gamma\!\left(
q(H)\left\lceil\sqrt{r+1}\right\rceil
\right).
}
\tag{6.4}
\]

Using (6.2) and (6.3), the right-hand side is polynomial in \(h\) and \(r\). In particular, if \(G\) has no two disjoint \(H\)-models, then \(r\le1\) and

\[
\tau_H(G)\le\gamma(2q(H))=h^{O(1)}.
\]

Thus the \(k=2\) obstruction has polynomial dependence on \(|H|\) for every connected planar \(H\).

---

## 7. Why the argument stops short of the full conjecture

The bound (6.4) is much too large when \(r\) is unbounded. Substituting the polynomial excluded-grid estimate gives only

\[
\tau_H(G)
\le h^{O(1)}r^{\,1+d/2},
\]

rather than \(h^{O(1)}r\log(r+1)\).

Nor can one expect a width estimate of the form

\[
\operatorname{tw}(G)\le a(H)\nu_H(G)
\]

for cyclic \(H\). For example, let \(H=K_3\), so that \(H\)-models are cycles. Standard fixed-degree high-girth expanders \(G_n\) satisfy

\[
\operatorname{tw}(G_n)=\Omega(n),
\qquad
\operatorname{girth}(G_n)=\Omega(\log n).
\]

Every cycle uses at least the girth number of vertices, so

\[
\nu_{K_3}(G_n)\le
\frac{n}{\operatorname{girth}(G_n)}
=O\!\left(\frac{n}{\log n}\right).
\]

Moreover, in a \(d\)-regular graph, deleting \(x\) vertices removes at most \(dx\) edges. If the remainder is a forest, then

\[
\frac{dn}{2}-dx\le n-x,
\]

which implies

\[
x\ge \frac{d-2}{2(d-1)}n.
\]

Thus

\[
\tau_{K_3}(G_n)=\Omega(n)
=\Omega\!\left(\nu_{K_3}(G_n)\log(\nu_{K_3}(G_n)+1)\right).
\]

This shows both that the logarithm is genuinely necessary and that a separator recursion based only on treewidth naturally risks paying that logarithm once for width and again for recursion. Avoiding this second payment, while retaining polynomial dependence on \(h\), is precisely the unresolved difficulty.

## 8. Remaining gap

The arguments above do not produce a bound

\[
c_*(H)\le |V(H)|^{O(1)}
\]

for arbitrary connected planar \(H\) containing cycles, nor do they handle disconnected planar patterns through the connected-model separator argument. They also give no superpolynomial lower bound or counterexample.

The firm conclusions are therefore:

\[
c_*(H)=\Omega(|V(H)|)
\]

for every \(H\);

\[
c_*(T)=\Theta(|V(T)|)
\]

for every tree \(T\); and the potential obstruction to polynomial dependence for general connected planar \(H\) can only appear in the unbounded-packing regime, not already at \(k=2\).