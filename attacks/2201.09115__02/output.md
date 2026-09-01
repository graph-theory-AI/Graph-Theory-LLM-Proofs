```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The Woodall bound holds when min{s,t}≤2; for general fixed s, any counterexample has a list-critical core on at least 2(s+t) vertices, while a construction shows that degeneracy alone cannot prove the conjecture for s≥10.",
  "would_publish": false,
  "caveats": "The cases of fixed s≥3 remain unresolved; the reductions use established theorems of Kostochka, Ohba, and Chudnovsky–Reed–Seymour."
}
```

## 1. Statement and notation

All graphs are finite and simple. Write
\[
k=s+t-1.
\]
The question is whether, for every fixed \(s\), all sufficiently large \(t\) have the property that every \(K_{s,t}\)-minor-free graph is \(k\)-choosable.

I prove three partial results:

1. The assertion holds for all \(s,t\) with \(\min\{s,t\}\le 2\).
2. Assuming \(t\) is in the range of Kostochka's fixed-\(s\) chromatic theorem, every counterexample contains a \(K_{s,t}\)-minor-free subgraph \(H\) satisfying
   \[
   |V(H)|\ge 2(s+t),\qquad
   \delta(H)\ge k,\qquad
   \Delta(H)\ge k+1,
   \]
   and
   \[
   \chi(H)\le k<\chi_\ell(H).
   \]
3. For every fixed \(s\ge10\), there are infinitely many \(t\) for which a \(K_{s,t}\)-minor-free graph has degeneracy exactly \(k\). Thus the natural strengthening “every such graph is \((k-1)\)-degenerate” is false even in the fixed-\(s\) regime. These examples are nevertheless \(k\)-choosable.

---

## 2. The cases \(\min\{s,t\}\le2\)

### The case \(s=1\)

If \(G\) has no \(K_{1,t}\) minor, then in particular it has no \(K_{1,t}\) subgraph. Hence
\[
\Delta(G)\le t-1.
\]
Greedy list coloring therefore shows that \(G\) is \(t\)-choosable, which is exactly
\[
s+t-1=t.
\]

This is sharp: \(K_t\) has no \(K_{1,t}\) minor and has list chromatic number \(t\).

### The case \(s=2\)

I use the exact density theorem of Chudnovsky, Reed and Seymour from *The edge-density for \(K_{2,t}\) minors*:

> **\(K_{2,t}\)-density theorem.**  
> For every \(t\ge2\), if a graph \(J\) has no \(K_{2,t}\) minor, then
> \[
> |E(J)|\le \frac{t+1}{2}\bigl(|V(J)|-1\bigr).
> \]

Consequently, every nonempty \(K_{2,t}\)-minor-free graph \(J\) has average degree strictly less than \(t+1\), and hence has a vertex of degree at most \(t\).

Every subgraph of a \(K_{2,t}\)-minor-free graph is again \(K_{2,t}\)-minor-free. It follows that every such graph is \(t\)-degenerate. Given lists of size at least \(t+1\), remove vertices successively with degree at most \(t\), and color them in reverse order. At most \(t\) colors are forbidden at each step, so the coloring always extends.

Thus every \(K_{2,t}\)-minor-free graph is \((t+1)\)-choosable, exactly as Woodall's bound predicts.

Again this is sharp: \(K_{t+1}\) has too few vertices to contain a \(K_{2,t}\) minor, while
\[
\chi_\ell(K_{t+1})=t+1.
\]

By symmetry of \(K_{s,t}\), this proves the conjectured bound whenever
\[
\min\{s,t\}\le2.
\]

---

## 3. Necessary structure of any fixed-\(s\) counterexample

### 3.1 A minimal bad-list core

Suppose \(G\) is not \(k\)-choosable. Choose a bad list assignment \(L\) with \(|L(v)|=k\) for every vertex, and let \(H\) be an induced subgraph minimal subject to \(H\) not being \(L\)-colorable.

Then \(H\) is connected, and
\[
\delta(H)\ge k.
\]

Indeed, for every \(v\in V(H)\), minimality gives an \(L\)-coloring of \(H-v\). If \(d_H(v)\le k-1\), at most \(k-1\) colors in \(L(v)\) are used on its neighbors, so the coloring extends to \(v\), a contradiction.

Thus any counterexample contains a minor-free core with minimum degree at least \(s+t-1\). This condition alone, however, will be shown insufficient in Section 4.

### 3.2 A useful consequence of Ohba's theorem

The theorem formerly known as Ohba's conjecture, proved by Noel, Reed and Wu, states that
\[
|V(Q)|\le 2\chi(Q)+1
\quad\Longrightarrow\quad
\chi_\ell(Q)=\chi(Q).
\]

We need the following padded form.

> **Lemma.** If \(\chi(Q)\le k\) and \(|V(Q)|\le2k+1\), then \(Q\) is \(k\)-choosable.

**Proof.** If \(|V(Q)|<k\), this is immediate. Otherwise, start with a proper coloring of \(Q\) with at most \(k\) color classes and split color classes until there are exactly \(k\) nonempty stable sets. Add all edges between distinct stable sets. The resulting supergraph \(Q'\) is complete \(k\)-partite, so
\[
\chi(Q')=k,\qquad |V(Q')|=|V(Q)|\le2k+1.
\]
Ohba's theorem gives \(\chi_\ell(Q')=k\). Since \(Q\subseteq Q'\),
\[
\chi_\ell(Q)\le\chi_\ell(Q')=k.
\]
\(\square\)

### 3.3 Applying Kostochka's chromatic theorem

The prompt reports the following settled chromatic statement:

> For each fixed \(s\), there exists \(T_s\) such that whenever \(t\ge T_s\), every \(K_{s,t}\)-minor-free graph is \((s+t-1)\)-colorable.

Assume \(t\ge T_s\), and let \(H\) be the minimal bad-list core above. Then
\[
\chi(H)\le k.
\]
If \(|V(H)|\le2k+1\), the padded Ohba lemma would imply that \(H\) is \(k\)-choosable, contrary to its construction. Therefore
\[
|V(H)|\ge2k+2=2(s+t).
\]

There is also a maximum-degree restriction. For \(k\ge3\), if \(\Delta(H)\le k\), then \(\delta(H)\ge k\) makes \(H\) \(k\)-regular. The list version of Brooks' theorem says that a connected \(k\)-regular graph is \(k\)-choosable unless it is \(K_{k+1}\) or, when \(k=2\), an odd cycle. Here \(K_{k+1}=K_{s+t}\) contains \(K_{s,t}\) as a subgraph. Hence
\[
\Delta(H)\ge k+1.
\]

We have therefore proved:

> **Critical-core reduction.**  
> For each fixed \(s\), once \(t\) is in the range of Kostochka's chromatic theorem, every counterexample contains a \(K_{s,t}\)-minor-free subgraph \(H\) such that
> \[
> |V(H)|\ge2(s+t),\qquad
> \delta(H)\ge s+t-1,\qquad
> \Delta(H)\ge s+t,
> \]
> and
> \[
> \chi(H)\le s+t-1<\chi_\ell(H).
> \]

Thus a counterexample cannot be a near-spanning obstruction on only \(s+t+O(1)\) vertices; it must have a genuinely large chromatic/list-chromatic gap.

---

## 4. Minimum degree and degeneracy do not suffice

One tempting strategy would be to prove that every \(K_{s,t}\)-minor-free graph has a vertex of degree at most \(k-1=s+t-2\), and then apply greedy list coloring. This works for \(s=2\), but it is false for fixed sufficiently large \(s\).

### 4.1 A high-girth neighborhood lemma

Let \(F\) be a \(d\)-regular graph of girth greater than \(2r\). For \(A\subseteq V(F)\), let \(N_F[A]\) denote its closed neighborhood.

> **Lemma.** If \(|A|=r\), then
> \[
> |N_F[A]|\ge(d-1)r+2.
> \]

**Proof.** Put \(B=N_F(A)\setminus A\), and let \(J\) consist of the vertices \(A\cup B\) and all edges of \(F\) having at least one endpoint in \(A\).

Any cycle in \(J\) uses at most \(r\) vertices of \(A\), and no two vertices of \(B\) are consecutive on such a cycle. Hence any cycle in \(J\) would have length at most \(2r\), contrary to the girth assumption. Thus \(J\) is a forest.

Let \(e_A=|E(F[A])|\) and let \(c\) be the number of components of \(J\). Summing degrees over \(A\),
\[
|E(J)|=dr-e_A.
\]
Since \(J\) is a forest,
\[
dr-e_A=r+|B|-c.
\]
Consequently
\[
|N_F[A]|=r+|B|=dr-e_A+c.
\]
Also \(F[A]\) is a forest, so \(e_A\le r-1\), while \(c\ge1\). Therefore
\[
|N_F[A]|\ge dr-(r-1)+1=(d-1)r+2.
\]
\(\square\)

### 4.2 The construction

Fix integers \(d\ge3\) and \(s>d\) satisfying
\[
(d-2)s>d^2+d-2. \tag{1}
\]
Equivalently, with \(r=s-d\),
\[
(d-1)r+2>s+2d. \tag{2}
\]

Choose a finite \(d\)-regular graph \(F_0\) of girth greater than \(2r\). Such regular graphs of arbitrarily prescribed fixed girth exist by the standard configuration-model argument. Let \(F\) be the disjoint union of \(m\) copies of \(F_0\), and write
\[
n=|V(F)|,\qquad t=n-s-d.
\]
For arbitrarily large \(m\), this gives arbitrarily large positive \(t\). Set
\[
G=\overline F.
\]
Since \(F\) is \(d\)-regular,
\[
G\text{ is }(n-1-d)\text{-regular}.
\]
But \(n=s+t+d\), so
\[
n-1-d=s+t-1=k.
\]
Thus \(G\) is \(k\)-regular and has degeneracy exactly \(k\).

I claim that \(G\) has no \(K_{s,t}\) minor. Suppose otherwise, and consider a minor model. There are \(s+t\) branch sets and only
\[
n-(s+t)=d
\]
surplus vertices. Hence at most \(d\) branch sets are nonsingletons. In particular:

- at least \(s-d=r\) branch sets on the \(s\)-side are singletons;
- at least \(t-d\) branch sets on the \(t\)-side are singletons.

Let \(A\) be the vertices of \(r\) singleton branch sets on the \(s\)-side, and let \(B\) be all singleton branch vertices on the \(t\)-side. Then
\[
|B|\ge t-d.
\]
Every vertex of \(A\) is adjacent in \(G\) to every vertex of \(B\), so there are no \(F\)-edges between \(A\) and \(B\). Consequently
\[
N_F[A]\subseteq V(F)\setminus B,
\]
and hence
\[
|N_F[A]|
\le n-|B|
\le s+t+d-(t-d)
=s+2d.
\]
On the other hand, the high-girth lemma gives
\[
|N_F[A]|\ge(d-1)(s-d)+2>s+2d,
\]
a contradiction. Thus \(G\) is \(K_{s,t}\)-minor-free.

Taking \(d=4\), condition (1) becomes
\[
2s>18,
\]
which holds for every \(s\ge10\). Therefore:

> **Degeneracy obstruction.**  
> For every fixed \(s\ge10\), there are infinitely many \(t\) for which a \(K_{s,t}\)-minor-free graph has minimum degree, maximum degree, and degeneracy all equal to \(s+t-1\).

These graphs are not counterexamples to Woodall's list bound. For sufficiently large \(n\), the \(k\)-regular graph \(G\) is connected: otherwise every component would have at least \(k+1=n-d\) vertices, forcing \(n\le2d\). It is neither complete nor an odd cycle, so the list version of Brooks' theorem gives
\[
\chi_\ell(G)\le k.
\]

Thus the construction only proves that the fixed-\(s\) problem cannot be settled by showing \((s+t-2)\)-degeneracy or by a minimum-degree forcing statement.

---

## 5. Remaining gap

The original question remains open for every fixed \(s\ge3\). The results above leave the following sharply defined obstruction.

For \(t\) sufficiently large in terms of \(s\), a counterexample must contain a graph \(H\) with
\[
|V(H)|\ge2(s+t),\qquad
\delta(H)\ge s+t-1,\qquad
\Delta(H)\ge s+t,
\]
which is \(K_{s,t}\)-minor-free and satisfies
\[
\chi(H)\le s+t-1<\chi_\ell(H).
\]

The \(s=2\) argument works because an exact minor-density theorem forces degeneracy below the list bound. The high-girth complement construction shows that this particular mechanism already fails for fixed \(s\ge10\). What is still missing is a way to exploit the stronger structure of a large, irregular list-critical graph rather than minimum degree alone.