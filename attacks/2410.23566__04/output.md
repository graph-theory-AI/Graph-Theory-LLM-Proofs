```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but every admissible constant must satisfy C at least 2, one-sided extensions satisfy u(D) at most 2^k u(F), and every extension reduces to a fully mixed core.",
  "would_publish": false,
  "caveats": "Assumes n at least 2 and the standard definition that added universal vertices are universal in the whole digraph; the Corollary 25 consequence retains its large-n hypothesis."
}
```

# Mathematical writeup

## 1. Conventions and immediate obstruction

For an acyclic digraph \(H\), let \(u(H)\) denote the least integer \(N\) such that every \(N\)-vertex tournament contains \(H\) as a not necessarily induced subdigraph. Integer roundings are suppressed below.

I use \(n\) for the order of the underlying oriented tree \(F\), as in the supplied abstract. I also assume \(n\ge 2\): for \(n=1\), the displayed bound \(C^k(2n-2)\) is zero, so the literal statement is false.

If \(k=0\) is included in “every integer \(k\),” then the conjecture specializes to
\[
u(F)\le 2n-2
\]
for every \(n\)-vertex oriented tree \(F\), exactly the unresolved finite form of Sumner's conjecture. Thus a complete proof necessarily includes that case. The arguments below give unconditional information for \(k\ge1\) and exact reductions for special extension patterns.

Write \(T_r\) for the transitive tournament of order \(r\), and write
\[
A\Rightarrow B
\]
for the digraph obtained from disjoint \(A,B\) by adding every arc from \(A\) to \(B\).

---

## 2. Normal form for a \(k\)-extension

Let \(D\) be an acyclic \(k\)-extension of an oriented tree \(F\), and let
\[
X=\{x_1,\dots,x_k\}
\]
be the added universal vertices. Since \(D[X]\) is an acyclic tournament, it is transitive; index it so that
\[
x_i\to x_j\qquad(i<j).
\]

For every \(v\in V(F)\), the tournament \(D[X\cup\{v\}]\) is also acyclic and hence transitive. Therefore there is a unique label
\[
\ell(v)\in\{0,\dots,k\}
\]
such that
\[
x_i\to v\quad\Longleftrightarrow\quad i\le \ell(v).
\tag{2.1}
\]
Thus \(v\) occupies the slot between \(x_{\ell(v)}\) and \(x_{\ell(v)+1}\).

The labeling is monotone along tree arcs:

**Lemma 2.1.** If \(u\to v\) is an arc of \(F\), then \(\ell(u)\le\ell(v)\).

**Proof.** If \(\ell(u)>\ell(v)\), choose \(i\) with
\[
\ell(v)<i\le\ell(u).
\]
Then (2.1) gives
\[
x_i\to u,\qquad u\to v,\qquad v\to x_i,
\]
a directed triangle, contrary to acyclicity. \(\square\)

Let
\[
a=\min_{v\in V(F)}\ell(v),\qquad b=\max_{v\in V(F)}\ell(v),
\]
and put
\[
s=b-a.
\]
Then:

- \(x_1,\dots,x_a\) dominate all of \(F\);
- \(x_{b+1},\dots,x_k\) are dominated by all of \(F\);
- each \(x_i\) with \(a<i\le b\) has both an in-neighbor and an out-neighbor in \(F\).

Call these last \(s\) vertices the **mixed universal vertices**, and let
\[
D^\ast=D\big[V(F)\cup\{x_{a+1},\dots,x_b\}\big].
\]
There is an exact ordinal decomposition
\[
D=T_a\Rightarrow D^\ast\Rightarrow T_{k-b}.
\tag{2.2}
\]

Thus every extension consists of a fully mixed core, padded on the two sides by globally one-sided universal vertices.

---

## 3. A sharp halving lemma for one-sided vertices

**Lemma 3.1.** For every oriented graph \(H\) and all \(p,q\ge0\),
\[
u(T_p\Rightarrow H\Rightarrow T_q)
   \le 2^{p+q}u(H).
\tag{3.1}
\]

**Proof.** Put \(m=u(H)\), and let \(R\) be any tournament on \(2^{p+q}m\) vertices.

Every tournament on \(2r\) vertices has a vertex with at least \(r\) out-neighbors, since its average out-degree is \(r-\tfrac12\). Starting with \(R\), choose successively \(p\) vertices \(y_1,\dots,y_p\), at each step retaining exactly half of the current tournament inside the out-neighborhood of the chosen vertex. The retained tournament has order \(2^q m\), and
\[
y_i\to y_j\quad(i<j),
\]
while every \(y_i\) dominates the retained tournament.

Now construct the terminal transitive tournament in reverse order. In the current tournament choose \(z_q\) with at least half the vertices as in-neighbors and retain that many in-neighbors. Next choose \(z_{q-1}\) similarly, and continue. The final retained set \(W\) has order \(m\), and
\[
z_i\to z_j\quad(i<j),
\]
while every vertex of \(W\) dominates every \(z_j\). All \(y_i\) dominate \(W\) and all the \(z_j\).

By the definition of \(m\), \(R[W]\) contains \(H\), giving the desired copy of
\[
T_p\Rightarrow H\Rightarrow T_q.
\]
\(\square\)

Applying this to (2.2) gives the following exact reduction.

**Corollary 3.2.**
\[
u(D)\le 2^{k-s}u(D^\ast).
\tag{3.2}
\]

Consequently, all the difficulty is concentrated in extensions in which every added universal vertex is mixed.

---

## 4. Uniform extensions: the conjectured exponential dependence holds

Suppose all tree vertices have the same label \(r\). Equivalently, no added universal vertex is mixed. Then
\[
D=T_r\Rightarrow F\Rightarrow T_{k-r},
\]
and Lemma 3.1 gives
\[
u(D)\le 2^k u(F).
\tag{4.1}
\]

Let \(A\ge1\) be any absolute constant for the linear unavoidability theorem for oriented trees quoted in the source, so that
\[
u(F)\le An.
\]
For \(k\ge1\) and \(n\ge2\), (4.1) gives
\[
u(D)\le A2^k n
   \le (2A)^k(2n-2).
\tag{4.2}
\]
Thus Conjecture 10 holds unconditionally for this entire subclass.

More precisely, for every individual tree satisfying the exact Sumner bound,
\[
u(F)\le2n-2,
\]
one obtains
\[
u(D)\le2^k(2n-2).
\tag{4.3}
\]
Hence \(C=2\) suffices for uniform extensions whenever the underlying tree satisfies the exact Sumner bound.

Lemma 3.1 also proves multiplicative stability with factor \(2\) when the newly added vertex is a global source or a global sink. It does not address a vertex having prescribed in- and out-neighbors in the old digraph.

---

## 5. Consequences for extensions with few mixed vertices

Equation (3.2) can be combined directly with the bound quoted from Corollary 25. Whenever that corollary applies to the \(s\)-extension \(D^\ast\),
\[
u(D^\ast)
 \le
 2\cdot 3^{\binom{2s+2}{2}}\lvert V(D^\ast)\rvert,
\]
and therefore
\[
u(D)
 \le
 2^{k-s+1}3^{\binom{2s+2}{2}}\lvert V(D^\ast)\rvert.
\tag{5.1}
\]
This improves the dependence on the total number \(k\) whenever many of the universal vertices are globally one-sided.

In particular,
\[
\binom{2s+2}{2}=2s^2+3s+1.
\]
Thus (5.1) has dependence
\[
\exp\!\big(O(k+s^2)\big)
\]
rather than \(\exp(O(k^2))\). If \(s\le c\sqrt{k}\), this is \(C_c^k\).

For example, if \(n>k\), \(s\le c\sqrt{k}\), and the large-\(n\) hypothesis of Corollary 25 holds, then
\[
|V(D^\ast)|=n+s<2n
\]
and
\[
u(D)\le
4\left(2\cdot 3^{\,2c^2+3c+1}\right)^k n.
\]
For \(k\ge1\), this is at most
\[
\left(8\cdot3^{\,2c^2+3c+1}\right)^k(2n-2).
\tag{5.2}
\]
The numerical constant is deliberately crude. The point is that the desired simple-exponential form follows whenever the number of mixed universal vertices is \(O(\sqrt{k})\), under the same size hypothesis as the quoted corollary.

For every fixed \(s_0\), the source theorem for fixed-size extensions, together with (3.2), also implies that there is a constant \(C(s_0)\) such that the conjectured form holds for all extensions having at most \(s_0\) mixed universal vertices. This remains only a structural special case because \(C(s_0)\) is not uniform in \(s_0\).

---

## 6. A second unconditional range: \(n=O(k)\)

Every acyclic digraph \(H\) on \(h\) vertices is a subdigraph of \(T_h\): take a topological ordering of \(H\) and add every missing forward arc. The standard induction gives
\[
u(T_h)\le2^{h-1},
\]
because every \(2^{h-1}\)-vertex tournament has a vertex with an in- or out-neighborhood of size at least \(2^{h-2}\).

A \(k\)-extension of an \(n\)-vertex tree has \(h=n+k\) vertices, so
\[
u(D)\le2^{n+k-1}.
\tag{6.1}
\]
Consequently, for every fixed \(\alpha\), the desired exponential form holds throughout the range \(n\le\alpha k\), with \(C=2^{\alpha+1}\). In particular, if \(n\le k\), then \(C=4\) suffices.

There is a sharper observation at \(n=2\). In that case every \(k\)-extension is an acyclic tournament on \(k+2\) vertices, hence is \(T_{k+2}\). Therefore
\[
u(D)\le2^{k+1}=2^k(2n-2),
\]
so \(C=2\) works for all extension patterns when \(n=2\).

---

## 7. A probabilistic lower bound: necessarily \(C\ge2\)

The base \(2\) in Lemma 3.1 cannot be replaced by any smaller absolute exponential base.

Fix an oriented tree \(F\) of order \(n\), and consider the valid \(k\)-extension
\[
H_{k,F}=T_k\Rightarrow F,
\]
in which all added universal vertices dominate the tree.

For a set \(S\) in a tournament, write
\[
N^+(S)=\bigcap_{x\in S}N^+(x).
\]
Every copy of \(H_{k,F}\) requires a \(k\)-set \(S\) whose common out-neighborhood has at least \(n\) vertices.

**Proposition 7.1.** Let \(0<\varepsilon<1\), and put
\[
N=\left\lfloor(1-\varepsilon)2^k n\right\rfloor.
\]
If
\[
k\log N<\frac{\varepsilon^2 n}{2},
\tag{7.1}
\]
then there is an \(N\)-vertex tournament containing no \(H_{k,F}\).

**Proof.** Orient every edge of \(K_N\) independently and uniformly. For any fixed \(k\)-set \(S\),
\[
X_S:=|N^+(S)|
\]
has distribution
\[
\operatorname{Bin}(N-k,2^{-k}),
\]
because each vertex outside \(S\) is dominated by all vertices of \(S\) with probability \(2^{-k}\), independently of the other outside vertices. Its mean satisfies
\[
\mu\le(1-\varepsilon)n.
\]

The multiplicative Chernoff bound gives
\[
\Pr(X_S\ge n)
 \le
 \exp\left(-\frac{(n-\mu)^2}{n+\mu}\right)
 \le
 \exp\left(-\frac{\varepsilon^2 n}{2}\right).
\]
Taking the union bound over all \(k\)-sets,
\[
\Pr\big(\exists S:\ |N^+(S)|\ge n\big)
 \le
 \binom Nk e^{-\varepsilon^2n/2}
 \le
 \exp\left(k\log N-\frac{\varepsilon^2n}{2}\right)<1
\]
by (7.1). Hence some tournament has every \(k\)-set with fewer than \(n\) common out-neighbors, and this tournament avoids \(H_{k,F}\). \(\square\)

For example, take \(\varepsilon=\tfrac12\) and \(n=k^3\). Condition (7.1) holds for all sufficiently large \(k\), yielding
\[
u(H_{k,F})>2^{k-1}k^3.
\tag{7.2}
\]

Now suppose the conjecture held with a constant \(C<2\). For \(n=k^3\),
\[
C^k(2n-2)
   \le 2C^k k^3
   <2^{k-1}k^3
\]
for all sufficiently large \(k\). An induced subtournament of the \(H_{k,F}\)-free tournament from (7.2), of order \(\lceil C^k(2n-2)\rceil\), would still avoid \(H_{k,F}\), contradicting the conjecture.

Therefore:

\[
\boxed{C\ge2\text{ for every constant }C\text{ satisfying Conjecture 10}.}
\]

More generally, Proposition 7.1 gives
\[
u(T_k\Rightarrow F)>(1-\varepsilon)2^k n
\]
whenever \(\varepsilon^2n\) is sufficiently larger than \(k\log(2^kn)\). Combined with (4.1), this shows that \(2^k n\) is the correct order for one-sided extensions.

---

## 8. What remains open

The preceding argument does not control the fully mixed core \(D^\ast\). When \(s=k\), reduction (3.2) gives no improvement, and the quoted bound remains
\[
3^{2k^2+O(k)}\,|V(D^\ast)|.
\]
The missing step is a bound of the form
\[
u(D^\ast)\le C^k n
\]
when every universal vertex has both an in-neighbor and an out-neighbor in the tree. In the normal form, this asks for a transitive \(k\)-tuple together with sufficiently rich reservoirs in several prescribed slots; simple repeated halving controls one common slot but not several slots simultaneously.

Thus there is neither a proof nor a counterexample here. The rigorous progress is:

1. every admissible constant must satisfy \(C\ge2\);
2. \(C=2\) is the correct base for globally one-sided padding;
3. arbitrary extensions reduce exactly to their fully mixed core;
4. the conjectured form holds for uniform extensions, for \(n=O(k)\), and—using the source bound—for extensions with sufficiently few mixed universal vertices;
5. the general fully mixed case, as well as the \(k=0\) Sumner case if included, remains unresolved.