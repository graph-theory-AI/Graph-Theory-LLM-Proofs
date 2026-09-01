```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A Ramsey-to-edit-distance transfer gives h(n,k,K_4)=Omega(n^2/(k^{3/2}(log k)^2)) and weaker general lower bounds, but it does not remove the logarithmic gap or settle r at least 5.",
  "would_publish": false,
  "caveats": "The argument uses established off-diagonal Ramsey lower bounds; for K_4 it determines the conjectured power of k but not the constant-factor asymptotics."
}
```

# Mathematical writeup

## 1. Statement and notation

For a graph \(G\), let
\[
\tau_k(G):=\min_{\phi:V(G)\to[k]}
 \bigl|\{uv\in E(G):\phi(u)=\phi(v)\}\bigr|.
\]
This equals the minimum number of edges that must be deleted from \(G\) to make it \(k\)-colorable. Thus
\[
h(n,k,K_r)=\max\{\tau_k(G): |V(G)|=n,\;G\text{ is }K_r\text{-free}\}.
\]

The conjecture asks whether, for every fixed \(r\ge3\),
\[
h(n,k,K_r)=\Theta_r\left(\frac{n^2}
 {k^{(r-1)/(r-2)}}\right)
\]
whenever \(n\) is sufficiently large in terms of \(k\).

I do not prove this. I prove a general transfer lemma from off-diagonal Ramsey constructions. Combining it with the recent lower bound for \(R(4,t)\) gives
\[
\boxed{
h(n,k,K_4)\ge
c\,\frac{n^2}{k^{3/2}(\log k)^2}
}
\]
for all sufficiently large \(k\) and all sufficiently large \(n=n(k)\). Consequently
\[
h(n,k,K_4)=n^2 k^{-3/2+o(1)}.
\]
Thus the conjectured power of \(k\) is correct for \(r=4\), although the requested constant-factor lower bound remains open.

For fixed \(r\ge5\), the standard \(K_r\)-free-process Ramsey bound similarly gives
\[
h(n,k,K_r)\ge
c_r\frac{n^2}{
 k^{(r+1)/(r-1)}(\log k)^{\eta_r}},
\qquad
\eta_r=\frac{r^2-r-4}{(r-1)(r-2)}.
\]

---

## 2. A weighted inequality

We use the following consequence of the Motzkin–Straus theorem.

### Lemma 2.1

Let \(F\) be a graph with independence number \(a=\alpha(F)\). For all nonnegative real numbers \((x_v)_{v\in V(F)}\),
\[
\sum_{uv\in E(F)}x_ux_v
\ge
\frac1{2a}\left(\sum_vx_v\right)^2
-\frac12\sum_vx_v^2.
\]

### Proof

Let \(\overline F\) denote the complement of \(F\). Its clique number is
\(\omega(\overline F)=a\). The weighted Motzkin–Straus inequality gives
\[
\sum_{uv\in E(\overline F)}x_ux_v
\le
\frac{a-1}{2a}\left(\sum_vx_v\right)^2.
\]
Since
\[
\sum_{\{u,v\}\subseteq V(F)}x_ux_v
=
\frac12\left(\left(\sum_vx_v\right)^2-\sum_vx_v^2\right),
\]
subtracting the contribution of \(E(\overline F)\) proves the claim.

For completeness, the weighted Motzkin–Straus inequality follows by normalizing \(\sum_vx_v=1\) and choosing a maximizer of minimum support. If two support vertices are nonadjacent, their total weight can be shifted entirely to one of them without decreasing the objective, contradicting minimality of the support. Thus the support is a clique of size at most \(a\), where the result follows from Cauchy–Schwarz. \(\square\)

---

## 3. Blow-ups of Ramsey graphs are far from \(k\)-colorable

### Proposition 3.1

Let \(F\) be a \(K_r\)-free graph on \(v\) vertices with independence number \(a\). If
\[
v\ge 2ak,
\]
then, for every \(n\ge2v\), there is a \(K_r\)-free graph \(G\) on \(n\) vertices satisfying
\[
\tau_k(G)\ge \frac{n^2}{8v}.
\]

### Proof

First suppose \(n=sv\). Replace each vertex \(u\in V(F)\) by an independent cluster \(V_u\) of size \(s\), and replace every edge \(uv\in E(F)\) by the complete bipartite graph between \(V_u\) and \(V_v\). Call the resulting balanced blow-up \(F[s]\).

Any clique in \(F[s]\) uses at most one vertex from each cluster and projects to a clique in \(F\). Hence \(F[s]\) is \(K_r\)-free.

Fix an arbitrary coloring
\[
\phi:V(F[s])\to[k].
\]
For \(u\in V(F)\) and \(c\in[k]\), put
\[
x_{u,c}=\frac{|\phi^{-1}(c)\cap V_u|}{s}.
\]
Thus
\[
x_{u,c}\ge0,
\qquad
\sum_{c=1}^k x_{u,c}=1.
\]
Let
\[
S_c=\sum_{u\in V(F)}x_{u,c}.
\]

The number \(M\) of monochromatic edges under \(\phi\) is
\[
M=s^2\sum_{c=1}^k\sum_{uv\in E(F)}x_{u,c}x_{v,c}.
\]
Applying Lemma 2.1 separately to each color gives
\[
\frac{M}{s^2}
\ge
\frac1{2a}\sum_{c=1}^kS_c^2
-\frac12\sum_{u,c}x_{u,c}^2.
\]
Now
\[
\sum_{c=1}^kS_c=v,
\]
so Cauchy–Schwarz yields
\[
\sum_{c=1}^kS_c^2\ge \frac{v^2}{k}.
\]
Moreover, for each \(u\),
\[
\sum_cx_{u,c}^2\le\left(\sum_cx_{u,c}\right)^2=1,
\]
and hence
\[
\sum_{u,c}x_{u,c}^2\le v.
\]
Therefore
\[
M\ge
\frac{s^2}{2}\left(\frac{v^2}{ak}-v\right).
\]
Under \(v\ge2ak\), this is at least
\[
M\ge\frac{s^2v}{2}
=\frac{(sv)^2}{2v}.
\]
Since the coloring was arbitrary,
\[
\tau_k(F[s])\ge\frac{(sv)^2}{2v}.
\]

For arbitrary \(n\ge2v\), take
\[
s=\left\lfloor\frac nv\right\rfloor
\]
and add \(n-sv\) isolated vertices to \(F[s]\). Since \(sv\ge n-v\ge n/2\),
\[
\tau_k(G)\ge\frac{(sv)^2}{2v}\ge\frac{n^2}{8v}.
\]
\(\square\)

A convenient Ramsey-theoretic formulation follows immediately.

### Corollary 3.2

If there is a \(K_r\)-free graph \(F\) on \(v\) vertices with
\[
\alpha(F)<t
\qquad\text{and}\qquad
v\ge2kt,
\]
then, for every \(n\ge2v\),
\[
h(n,k,K_r)\ge\frac{n^2}{8v}.
\]

---

## 4. General transfer from Ramsey exponents

Let \(R(r,t)\) be the least \(N\) such that every \(N\)-vertex graph contains either a \(K_r\) or an independent set of size \(t\).

### Theorem 4.1

Suppose that, for some fixed \(r\), constants \(\beta>1\), \(\gamma\ge0\), and \(c>0\),
\[
R(r,t)\ge
c\,\frac{t^\beta}{(\log t)^\gamma}
\]
for all sufficiently large \(t\). Then there is \(c'>0\) such that, for all sufficiently large \(k\) and all sufficiently large \(n\) in terms of \(k\),
\[
h(n,k,K_r)\ge
c'\frac{n^2}{
 k^{\beta/(\beta-1)}
 (\log k)^{\gamma/(\beta-1)}}.
\]

### Proof

Choose
\[
t=
\left\lceil
A\,k^{1/(\beta-1)}
(\log k)^{\gamma/(\beta-1)}
\right\rceil,
\]
where \(A\) is a sufficiently large constant depending only on the constants in the Ramsey estimate. Put
\[
v=
\left\lfloor
\frac c2\,\frac{t^\beta}{(\log t)^\gamma}
\right\rfloor.
\]
The Ramsey hypothesis supplies a \(K_r\)-free graph on \(v\) vertices with independence number less than \(t\).

Because \(\log t=\Theta(\log k)\),
\[
\frac{v}{kt}
=\Theta\left(
\frac{t^{\beta-1}}{k(\log t)^\gamma}
\right).
\]
By taking \(A\) large, this ratio is at least \(2\). On the other hand, with \(A\) fixed, it is bounded above by a constant. Thus
\[
2kt\le v\le Ckt
\]
and
\[
v=
\Theta\left(
k^{\beta/(\beta-1)}
(\log k)^{\gamma/(\beta-1)}
\right).
\]
Corollary 3.2 now gives the result. \(\square\)

---

## 5. Application to \(K_4\)

Mattheus and Verstraëte proved in *The asymptotics of \(r(4,t)\)* that
\[
R(4,t)\ge
c\,\frac{t^3}{(\log t)^4}.
\]
Applying Theorem 4.1 with
\[
\beta=3,\qquad \gamma=4
\]
gives:

### Corollary 5.1

There are absolute constants \(c,C>0\) such that, for all sufficiently large \(k\) and
\[
n\ge Ck^{3/2}(\log k)^2,
\]
\[
\boxed{
h(n,k,K_4)\ge
c\,\frac{n^2}{k^{3/2}(\log k)^2}.
}
\]

Together with the Fox–Himwich–Mani upper bound,
\[
h(n,k,K_4)\le C'\frac{n^2}{k^{3/2}},
\]
this gives
\[
\frac{c\,n^2}{k^{3/2}(\log k)^2}
\le h(n,k,K_4)
\le
\frac{C'n^2}{k^{3/2}}.
\]
In particular,
\[
h(n,k,K_4)=n^2k^{-3/2+o(1)}.
\]

This does not establish the requested \(\Theta(n^2/k^{3/2})\), since the factor \((\log k)^2\) cannot be absorbed into a constant.

---

## 6. A general unconditional lower bound

The \(K_r\)-free-process results of Bohman and Keevash imply, for each fixed \(r\ge4\),
\[
R(r,t)\ge
c_r\frac{t^{(r+1)/2}}
 {(\log t)^{(r+1)/2-1/(r-2)}}.
\]
For \(r=4\), this is superseded here by the Mattheus–Verstraëte estimate. For \(r\ge5\), Theorem 4.1 gives:

### Corollary 6.1

For every fixed \(r\ge5\), there are constants \(c_r,C_r>0\) such that, for all sufficiently large \(k\) and
\[
n\ge
C_r k^{(r+1)/(r-1)}(\log k)^{\eta_r},
\]
where
\[
\eta_r
=
\frac{2}{r-1}
\left(\frac{r+1}{2}-\frac1{r-2}\right)
=
\frac{r^2-r-4}{(r-1)(r-2)},
\]
one has
\[
\boxed{
h(n,k,K_r)\ge
c_r
\frac{n^2}{
 k^{(r+1)/(r-1)}
 (\log k)^{\eta_r}}.
}
\]

For example,
\[
h(n,k,K_5)
\ge
c\,\frac{n^2}{k^{3/2}(\log k)^{4/3}},
\]
whereas the conjectured lower bound is of order \(n^2/k^{4/3}\).

The gap in the power of \(k\) is
\[
\frac{r+1}{r-1}-\frac{r-1}{r-2}
=
\frac{r-3}{(r-1)(r-2)}.
\]

---

## 7. Why this method stops short

The transfer argument uses a \(K_r\)-free template \(F\) with
\[
|V(F)|\gtrsim k\,\alpha(F).
\]
To obtain the conjectured lower bound solely through this method, one would seek a template with
\[
|V(F)|=O\left(k^{(r-1)/(r-2)}\right),
\qquad
\alpha(F)=O\left(k^{1/(r-2)}\right).
\]
Eliminating \(k\), this is the scale
\[
|V(F)|=\Theta\bigl(\alpha(F)^{\,r-1}\bigr),
\]
namely the extremal polynomial scale in the off-diagonal Ramsey problem.

This is only a limitation of the Ramsey-template method. It is not a converse: a graph far from \(k\)-colorable could conceivably have large independent sets and derive its obstruction from a more complicated distribution of edges.

A second elementary necessary condition is worth recording. Randomly assigning \(k\) colors gives
\[
\tau_k(G)\le\frac{e(G)}k.
\]
Thus any witness to the conjectured lower bound must have
\[
e(G)=\Omega_r\left(
\frac{n^2}{k^{1/(r-2)}}
\right).
\]
Producing such comparatively dense \(K_r\)-free graphs while maintaining robust obstruction to every \(k\)-coloring is the unresolved part.

## 8. Final status

- \(r=3\): settled in the source paper.
- \(r=4\): the conjectured exponent \(3/2\) is obtained up to a factor \((\log k)^2\).
- \(r\ge5\): the Ramsey-transfer lower bound above improves the universal triangle-free lower bound asymptotically, but a genuine polynomial gap remains.
- No proof or counterexample to the original constant-factor conjecture is obtained.