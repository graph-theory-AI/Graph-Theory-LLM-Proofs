```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A sharp stable-module lifting theorem gives explicit positive cases for every k≥3 and a gap-preserving parameter reduction, but does not settle the general conjecture.",
  "would_publish": false,
  "caveats": "The positive cases use the established k=2 theorem supplied in the question; no novelty claim is made for these restricted results."
}
```

## 1. Notation and scope

All digraphs below are finite and loopless. Opposite arcs are allowed. Coloring means ordinary coloring of the underlying undirected graph, so a color class contains no arc in either direction.

Write
\[
\pi_k(D)=\min_{\mathcal P}\sum_{P\in\mathcal P}\min\{|V(P)|,k\},
\qquad
\alpha_k(D)=\max\{|X|:D[X]\text{ is }k\text{-colorable}\}.
\]
The conjecture is \(\pi_k(D)\le \alpha_k(D)\).

I do not obtain a general proof or counterexample. The main result below is an unconditional extension theorem for both quantities. It yields a family satisfying the conjecture at every \(k\ge3\), with an arbitrary digraph as its core.

## 2. A stable-module lifting theorem

Let \(R\) be an \(n\)-vertex digraph. Add a set \(S\) of \(m\) new vertices such that:

- \(S\) is stable;
- every vertex of \(S\) is adjacent to every vertex of \(R\);
- the directions of these new adjacencies are otherwise arbitrary.

Thus the underlying graph of the resulting digraph \(D\) is
\[
G(D)=G(R)\vee \overline{K_m}.
\]

### Theorem

Let \(k\ge1\) and
\[
m\ge \left\lfloor\frac{n}{k+1}\right\rfloor.
\]
Then
\[
\boxed{\alpha_{k+1}(D)=m+\alpha_k(R)}
\tag{1}
\]
and
\[
\boxed{\pi_{k+1}(D)\le m+\pi_k(R).}
\tag{2}
\]

If, more specifically, every new arc is directed from \(S\) to \(R\), with no reverse arcs, then equality holds in (2):
\[
\boxed{\pi_{k+1}(D)=m+\pi_k(R).}
\tag{3}
\]

Consequently, arbitrary directions between \(S\) and \(R\) cannot increase the conjecture’s gap:
\[
\pi_{k+1}(D)-\alpha_{k+1}(D)
\le
\pi_k(R)-\alpha_k(R).
\tag{4}
\]
For the source extension in (3), the gaps are equal.

### Proof

#### An insertion observation

If \(P=v_1\cdots v_\ell\) is a directed path and \(x\) is adjacent to every vertex of \(P\), then \(P\cup\{x\}\) has a directed path using all its vertices.

Indeed:

- if \(xv_1\) is an arc, prepend \(x\);
- if \(v_\ell x\) is an arc, append \(x\);
- otherwise, let \(j\ge2\) be the first index for which \(xv_j\) is an arc. Such an index exists because \(xv_\ell\) is an arc. Adjacency and the choice of \(j\) give \(v_{j-1}x\), so insert \(x\) between \(v_{j-1}\) and \(v_j\).

This requires no adjacency between nonconsecutive vertices of \(P\).

#### The coloring identity

First, for every digraph \(R\),
\[
\alpha_{k+1}(R)
\le
\alpha_k(R)+\left\lfloor\frac{n}{k+1}\right\rfloor.
\tag{5}
\]
To see this, take a maximum \((k+1)\)-colorable induced subgraph and a coloring with \(k+1\) classes, allowing empty classes. Delete a smallest class. Its size is at most \(\lfloor n/(k+1)\rfloor\), and the remaining vertices are \(k\)-colorable.

Because \(S\) is stable and complete to \(R\),
\[
\alpha_{k+1}(D)
=
\max\{\alpha_{k+1}(R),\,m+\alpha_k(R)\}.
\tag{6}
\]
For the second term, use one color on all of \(S\) and \(k\) colors in \(R\). Conversely, any colored induced subgraph meeting \(S\) has a color used on \(S\) that cannot be used in \(R\); hence its part in \(R\) is \(k\)-colorable.

Equation (5) and the hypothesis on \(m\) show that the second term in (6) is at least the first. This proves (1). The case \(S=\varnothing\) under the stated size condition is immediate as well.

#### The path-partition inequality

Choose a path partition \(\mathcal P\) of \(R\) attaining \(\pi_k(R)\). Let
\[
q=\bigl|\{P\in\mathcal P:|V(P)|\ge k+1\}\bigr|.
\]
Vertex-disjointness gives
\[
q(k+1)\le n,
\qquad\text{so}\qquad q\le m.
\]

Assign a different vertex of \(S\) to each of these \(q\) long paths and insert it using the observation above. Leave the other \(m-q\) vertices of \(S\) as singleton paths.

Each long path contributed \(k\) to the old \(k\)-norm and contributes \(k+1\) to the new \((k+1)\)-norm. Every other old path has at most \(k\) vertices, so its contribution is unchanged. The resulting partition therefore has norm
\[
\pi_k(R)+q+(m-q)=\pi_k(R)+m.
\]
This proves (2).

#### Equality for added sources

Now suppose all arcs between the two sets are directed from \(S\) to \(R\).

Every directed path contains at most one vertex of \(S\), necessarily as its first vertex. Remove all vertices of \(S\) from an arbitrary path partition of \(D\), discarding empty paths. The remaining paths partition \(R\).

For a path containing a vertex of \(S\) followed by \(\ell\) vertices of \(R\),
\[
\min\{\ell+1,k+1\}=1+\min\{\ell,k\}.
\]
For a path lying wholly in \(R\),
\[
\min\{\ell,k+1\}\ge \min\{\ell,k\}.
\]
There are exactly \(m\) paths containing vertices of \(S\). Thus every path partition of \(D\) has \((k+1)\)-norm at least
\[
m+\pi_k(R).
\]
Together with (2), this proves (3). ∎

## 3. Unconditional cases at every \(k\ge3\)

The preceding theorem does not assume the conjecture. We can now apply it to the established \(k=2\) case supplied in the question.

### Corollary: a \(k=3\) family

Let \(R\) be any \(n\)-vertex digraph. Add a stable set \(S\), complete to \(R\), of size
\[
m\ge \left\lfloor\frac n3\right\rfloor.
\]
Allow arbitrary directions between \(S\) and \(R\). Then
\[
\pi_3(D)
\le m+\pi_2(R)
\le m+\alpha_2(R)
=\alpha_3(D).
\]

Thus the core \(R\) may be completely arbitrary; only the added stable module is prescribed.

### Corollary: a family for every larger parameter

Fix an arbitrary \(n\)-vertex digraph \(R\), an integer \(t\ge1\), and
\[
m\ge \left\lfloor\frac n3\right\rfloor.
\]
Add stable sets \(S_1,\dots,S_t\), each of size \(m\), making every pair of vertices in different sets adjacent and making every new vertex adjacent to every vertex of \(R\). All directions of these adjacencies may be chosen arbitrarily.

For the resulting digraph \(D\),
\[
\boxed{
\pi_{t+2}(D)
\le tm+\pi_2(R)
\le tm+\alpha_2(R)
=\alpha_{t+2}(D).
}
\tag{7}
\]

#### Proof

Let \(R_j\) be the subdigraph on \(R\cup S_1\cup\cdots\cup S_j\). At step \(j\), apply the theorem with old parameter \(j+1\). Its size condition is
\[
m\ge
\left\lfloor
\frac{n+(j-1)m}{j+2}
\right\rfloor.
\]
The initial assumption gives \(n\le3m+2\), and hence
\[
n+(j-1)m\le(j+2)m+2.
\]
Since \(j+2\ge3\), the required condition follows.

Iterating (1) and (2) gives the first and last relations in (7). The middle inequality is the known \(k=2\) theorem. ∎

Taking \(t=k-2\) proves an explicit class at every \(k\ge3\). This is not limited to acyclic cores, locally semicomplete cores, or cores satisfying any additional conjecture.

## 4. The source extension preserves the obstruction exactly

Define
\[
\delta_k(R)=\pi_k(R)-\alpha_k(R).
\]
For the source extension,
\[
\delta_{k+1}(D)=\delta_k(R).
\tag{8}
\]

This has two consequences.

1. **A counterexample at one parameter would give counterexamples at every larger parameter.**  
   The extension preserves the positive gap rather than merely preserving failure.

2. **The universal statement at parameter \(k+1\) implies the universal statement at parameter \(k\).**  
   Apply the former statement to the source extension of an arbitrary \(R\).

The size increase can be kept linear over repeated extensions. Write
\[
n=(k+1)m+r,\qquad
m=\left\lfloor\frac n{k+1}\right\rfloor,\quad 0\le r<k+1.
\]
After adding \(t\) source blocks of size \(m\), the graph has \(n+tm\) vertices, the parameter is \(k+t\), and the gap is still \(\delta_k(R)\). At each step the required floor remains \(m\).

This is an exact structural reduction, **not** a resolution by reduction to another conjecture: it explicitly shows that the unresolved obstruction survives the operation.

## 5. Sharpness of the uniform size threshold

The bound
\[
m\ge\left\lfloor\frac n{k+1}\right\rfloor
\]
cannot be lowered uniformly in \(n,k\) while retaining the path inequality (2).

Write
\[
n=q(k+1)+r,\qquad 0\le r<k+1.
\]
Let \(R\) be the disjoint union of \(q\) directed paths on \(k+1\) vertices and \(r\) isolated vertices. Then
\[
\pi_k(R)=qk+r=n-q.
\]

Add \(m<q\) independent universal sources. Every path in the resulting digraph has at most \(k+2\) vertices. A path of order \(k+2\) must contain a new source, so there can be at most \(m\) such paths. Consequently, the total saving in \((k+1)\)-norm relative to singletons is at most \(m\), giving
\[
\pi_{k+1}(D)\ge(n+m)-m=n.
\]
Equality is achieved by prefixing the \(m\) sources to \(m\) different original path components. Hence
\[
\pi_{k+1}(D)=n
>
n-q+m
=
m+\pi_k(R).
\]

These examples are **not counterexamples to Linial–Berge**. They show only that the lifting theorem’s uniform threshold is sharp.

## 6. A computational consequence on the proved subclass

For each fixed \(k\ge3\), computing \(\pi_k\) remains NP-hard even on the source-extension family in Section 3, with its decomposition supplied.

Indeed, start with an arbitrary digraph \(R\) on \(n\ge3\) vertices, set
\[
m=\left\lfloor\frac n3\right\rfloor,\qquad t=k-2,
\]
and add the \(t\) stable blocks successively as universal sources. Repeated equality in (3) gives
\[
\pi_k(D)=tm+\pi_2(R).
\]
For \(n\ge3\),
\[
\pi_2(R)\le2
\quad\Longleftrightarrow\quad
R\text{ has a directed Hamiltonian path}.
\]
Thus deciding whether \(\pi_k(D)\le tm+2\) is NP-hard by directed Hamiltonian path. The threshold decision problem is in NP because a path partition is a polynomially verifiable certificate.

This concerns computation of the left-hand optimum, not the truth of the conjecture: the conjecture holds on this entire subclass by (7).

## 7. Remaining gap

The construction needs a stable module large enough to supply one new vertex for every path whose norm increases when the parameter changes. Arbitrary digraphs need not contain such a module.

Therefore the unrestricted \(k=3\) case remains untouched. The exact source identity also explains why the extension cannot silently remove the main difficulty: for source extensions, it preserves that difficulty exactly.

The established output is a sharp extension theorem, explicit positive families for all \(k\ge3\), and an exact parameter relation. I make no claim that these elementary restricted results are new in the literature.