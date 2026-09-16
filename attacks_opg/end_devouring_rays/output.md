```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The supplied catalog records the resolution, and a minimum-distance prefix construction gives a self-contained proof.",
  "would_publish": false,
  "caveats": "No novelty is claimed; bibliographic attribution follows the supplied catalog."
}
```

The question itself records the published resolution by Gollin and Heuer. Below is a self-contained proof of the stated result, without invoking their theorem as a black box.

## Theorem

Let \(G\) be a graph, let \(\omega\) be a countable end of \(G\), and let \(K\) be an infinite family of pairwise vertex-disjoint \(\omega\)-rays. There is a family \(K'\) of pairwise vertex-disjoint \(\omega\)-rays which devours \(\omega\) and has precisely the same starting vertices as \(K\).

For a finite vertex set \(X\), write \(C(X,\omega)\) for the component of \(G-X\) containing a tail of every \(\omega\)-ray.

## 1. A countable, concentrated devouring set

By countability of \(\omega\), there is a countable vertex set \(A\) meeting every \(\omega\)-ray: take the union of the vertex sets of a countable devouring family.

Consequently, every family of pairwise disjoint \(\omega\)-rays is countable. Indeed, assigning to each ray its first intersection with a fixed enumeration of \(A\) gives an injection into \(A\). In particular, although \(K\) was only assumed infinite, it is countably infinite.

Extend \(K\), by Zorn’s lemma, to a maximal family \(\mathcal M\) of pairwise disjoint \(\omega\)-rays. This family is countable, and
\[
D:=\bigcup_{R\in\mathcal M}V(R)
\]
meets every \(\omega\)-ray, by maximality.

We also have the important concentration property
\[
D\setminus C(X,\omega)\text{ is finite for every finite }X\subseteq V(G).
\tag{1}
\]
To see this, only finitely many members of \(\mathcal M\) meet \(X\), since they are disjoint. Every member avoiding \(X\) lies entirely in \(C(X,\omega)\). Each member meeting \(X\) has only finitely many vertices outside that component.

Two consequences will be used:

* Every \(\omega\)-ray meets \(D\) infinitely often, since otherwise a tail would avoid \(D\).
* Every ray meeting \(D\) infinitely often belongs to \(\omega\). Indeed, after deleting any finite \(X\), its tail lies in one component; by (1), that component must be \(C(X,\omega)\).

Enumerate
\[
D=\{v_0,v_1,\ldots\},
\qquad
S=\{s_0,s_1,\ldots\},
\]
where \(S\) is the set of starting vertices of \(K\).

## 2. A prefix-forcing lemma

An **\(S\)-family** means a family \(\mathcal L=(L_s:s\in S)\) of pairwise disjoint \(\omega\)-rays, with \(L_s\) starting at \(s\).

A **prefix system** is a family
\[
\mathcal P=(P_s:s\in S)
\]
of pairwise disjoint finite paths starting at their respective \(s\), with only finitely many paths having an edge. It is **feasible** if some \(S\)-family extends all its paths as initial segments. Such an \(S\)-family is called a completion.

### Lemma
Given a feasible prefix system \(\mathcal P\) and a vertex \(v\), one can extend at most one of its paths, preserving feasibility, so that every completion of the enlarged system meets every \(\omega\)-ray starting at \(v\).

### Proof

Let \(t_s\) be the last vertex of \(P_s\), and put
\[
F=\bigcup_{s\in S}\bigl(V(P_s)\setminus\{t_s\}\bigr),
\qquad H=G-F.
\]
The set \(F\) is finite.

If \(v\notin C(F,\omega)\), every \(\omega\)-ray starting at \(v\) meets \(F\), which is contained in every completion. No extension is needed.

Suppose, therefore, that \(v\in C(F,\omega)\). For a completion \(\mathcal L\), let
\[
T(\mathcal L)
  =\bigcup_{s\in S}V\bigl(L_s[t_s,\infty)\bigr)
\]
be the union of its tails from the current tips. These tails lie in \(H\), and each has a tail in \(C(F,\omega)\). Hence
\[
d=\min_{\mathcal L\text{ completing }\mathcal P}
       d_H\bigl(v,T(\mathcal L)\bigr)
\tag{2}
\]
is a finite nonnegative integer.

Choose a completion \(\mathcal L^0\) attaining this minimum, and a vertex
\(z\in T(\mathcal L^0)\) with \(d_H(v,z)=d\). If \(z\in L^0_{s_*}\), extend \(P_{s_*}\) along \(L^0_{s_*}\) through \(z\), leaving all other prefixes unchanged. The resulting system is feasible.

Consider any completion \(\mathcal L\) of this enlarged system. Throughout the remainder of the proof, \(T(\mathcal L)\) is still defined using the **original** tips \(t_s\). Since the enlarged prefix fixes \(z\) on the appropriate tail,
\[
d_H\bigl(v,T(\mathcal L)\bigr)\le d_H(v,z)=d.
\]
The reverse inequality follows from (2), because \(\mathcal L\) also completes the original system. Thus
\[
d_H\bigl(v,T(\mathcal L)\bigr)=d.
\tag{3}
\]

Suppose there were an \(\omega\)-ray \(Q\) starting at \(v\) and disjoint from \(\mathcal L\). Then \(d\ge1\). Choose a shortest path in \(H\)
\[
W=v=w_0,w_1,\ldots,w_d=x
\]
from \(v\) to \(T(\mathcal L)\). All vertices of \(W\) other than \(x\) avoid \(T(\mathcal L)\). Since \(W\subseteq H\), they avoid the entire family \(\mathcal L\): its vertex union is \(F\cup T(\mathcal L)\).

Let \(x\in L_s[t_s,\infty)\). Starting at \(x\), traverse \(W\) towards \(v\), and let \(q\) be the first vertex encountered on \(Q\). Replace \(L_s\) by
\[
L_s[s,x]\; W[x,q]\; Q[q,\infty).
\tag{4}
\]
This concatenation is a ray: the interior of the connecting segment avoids \(\mathcal L\), and its portion before \(q\) avoids \(Q\). It is disjoint from all other \(L_{s'}\), belongs to \(\omega\), and preserves the original prefix \(P_s\).

Thus (4), together with the unchanged rays, is another completion \(\mathcal L'\) of the **original** prefix system. But \(w_{d-1}\) lies on its tail after \(t_s\), giving
\[
d_H\bigl(v,T(\mathcal L')\bigr)
 \le d_H(v,w_{d-1})=d-1,
\]
contrary to (2).

Therefore every completion of the enlarged system meets every \(\omega\)-ray starting at \(v\). ∎

The point of this lemma is that its conclusion survives all subsequent feasible prefix extensions.

## 3. Constructing the rays

Begin with the trivial prefixes
\[
P_s^0=(s)\qquad(s\in S).
\]
They form a feasible system, witnessed by \(K\).

Inductively suppose that \(\mathcal P^n=(P_s^n:s\in S)\) has been constructed.

1. Apply the lemma to \(\mathcal P^n\) and \(v_n\), obtaining an enlarged feasible system \(\widehat{\mathcal P}^{\,n}\). Every completion of this system meets every \(\omega\)-ray starting at \(v_n\).

2. Choose a completion \(\mathcal L^n\) of \(\widehat{\mathcal P}^{\,n}\).

3. For each \(i\le n\), extend the prefix belonging to \(s_i\) along \(L^n_{s_i}\) far enough to include a vertex of \(D\) strictly beyond its current last vertex. This is possible because every \(\omega\)-ray meets \(D\) infinitely often. Leave the other prefixes unchanged.

Call the resulting system \(\mathcal P^{n+1}\). It is feasible, witnessed by \(\mathcal L^n\), and still has only finitely many nontrivial paths. Moreover,
\[
P_s^n\subseteq P_s^{n+1}
\]
as initial segments, and the forcing conclusion for \(v_n\) remains valid.

For each \(s\in S\), define
\[
R_s=\bigcup_{n\ge0}P_s^n.
\]
If \(s=s_i\), its prefix grows at every stage \(n\ge i\), acquiring a new vertex of \(D\). Thus \(R_s\) is a ray meeting \(D\) infinitely often. By (1) and its consequence above, \(R_s\in\omega\).

The rays \(R_s\) are pairwise disjoint: any alleged common vertex would already appear in two paths at some finite stage. Therefore
\[
K'=\{R_s:s\in S\}
\]
is an \(S\)-family, and it completes every prefix system constructed above.

## 4. Verification of devouring

Let \(Q\) be any \(\omega\)-ray. Since \(D\) meets every such ray, choose
\[
v_n\in V(Q)\cap D.
\]
The tail \(Q[v_n,\infty)\) is an \(\omega\)-ray starting at \(v_n\).

At stage \(n\), the prefix-forcing lemma ensured that every completion of \(\widehat{\mathcal P}^{\,n}\) meets this tail. The final family \(K'\) is such a completion. Hence \(Q\) meets \(K'\).

Thus \(K'\) devours \(\omega\), and by construction its starting vertices are exactly \(S\), the starting vertices of \(K\). ∎

### Scope of the argument

No local finiteness assumption is used. In particular, the proof does not assume that limits of \(\omega\)-rays automatically remain in \(\omega\): the concentration property (1), together with the scheduled visits to \(D\), explicitly guarantees this. The only maximality principle used is Zorn’s lemma in constructing \(\mathcal M\).