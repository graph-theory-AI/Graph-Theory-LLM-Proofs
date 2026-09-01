```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A finite clique-covering hypergraph gives a computable density below which almost all Km copies survive, and a filtered Turan reduction isolates but does not solve the remaining threshold.",
  "would_publish": false,
  "caveats": "The exact hard-regime transition and critical scales remain open; the covering reduction likely overlaps arXiv:1806.06609."
}
```

## 1. Statement and normalization

Fix \(m\ge 2\) and a graph \(H\) with \(\chi(H)=k>m\). Put
\[
a=\binom m2,\qquad
\mu=\binom nm p^a,
\]
so that \(\mu\) is the expected number of copies of \(K_m\) in \(G(n,p)\). Define
\[
\rho=\rho_{k,m}
   :=\frac{m!\binom{k-1}{m}}{(k-1)^m}
   =\frac{(k-1)_m}{(k-1)^m}.
\]
Then the quantity in the question is
\[
\binom{k-1}{m}\left(\frac{n}{k-1}\right)^m p^a
   =(\rho+o(1))\mu.
\]
Notice that \(0<\rho<1\).

For every deterministic graph \(G\),
\[
\operatorname{ex}(G,K_m,H)\ge \rho\,N(K_m,G).
\]
Indeed, randomly color \(V(G)\) with \(k-1\) colors and retain only cross-edges. The resulting graph is \(H\)-free, and a given \(K_m\) survives with probability \(\rho\).

Thus the difficult direction is always the upper bound
\[
\operatorname{ex}(G(n,p),K_m,H)\le (\rho+o(1))\mu.
\]

The multiplicative assertion also requires
\[
\mu\longrightarrow\infty,
\qquad\text{equivalently}\qquad
p\gg n^{-2/(m-1)}.
\]
If \(\mu\) is bounded, the number of \(K_m\)'s has nonvanishing fluctuations, so it cannot be asymptotic with high probability to the deterministic quantity \(\rho\mu\).

The rest of the argument concerns \(m\ge3\), where the hard regime exists.

---

## 2. Exact reformulation as an independence problem

For a family \(\mathcal Q\) of distinct \(m\)-subsets, write
\[
V(\mathcal Q)=\bigcup_{Q\in\mathcal Q}Q,
\qquad
\partial_2\mathcal Q=\bigcup_{Q\in\mathcal Q}\binom Q2,
\]
and set
\[
v(\mathcal Q)=|V(\mathcal Q)|,\qquad
e(\mathcal Q)=|\partial_2\mathcal Q|.
\]

An **\(H\)-cover by \(K_m\)'s** is a pair consisting of an embedding
\(\phi:V(H)\hookrightarrow V(\mathcal Q)\) and a family \(\mathcal Q\) such that
\[
\phi(E(H))\subseteq \partial_2\mathcal Q.
\]
It is minimal if no proper subfamily of \(\mathcal Q\) still covers the same copy \(\phi(H)\).

Every member of a minimal cover contains an edge of \(\phi(H)\) that no other member covers. Consequently,
\[
2\le |\mathcal Q|\le e(H),
\qquad
v(\mathcal Q)\le v(H)+(m-2)e(H).
\]
The lower bound follows from \(\chi(H)>m\): one \(m\)-set cannot have a 2-shadow containing \(H\). Hence there are only finitely many isomorphism types of minimal covers.

For a graph \(G\), define a finite nonuniform hypergraph \(\mathcal A_{H,m}(G)\) whose vertices are the copies of \(K_m\) in \(G\), and whose hyperedges are the minimal \(H\)-covers consisting of these copies.

### Lemma 2.1
For every graph \(G\),
\[
\operatorname{ex}(G,K_m,H)=\alpha(\mathcal A_{H,m}(G)).
\]

#### Proof

If \(G'\subseteq G\) is \(H\)-free, then the family of all copies of \(K_m\) in \(G'\) contains no minimal \(H\)-cover. Thus
\[
N(K_m,G')\le \alpha(\mathcal A_{H,m}(G)).
\]

Conversely, let \(\mathcal S\) be an independent family of copies of \(K_m\) in \(G\), and let \(F\) be the graph obtained by taking the union of all edges of members of \(\mathcal S\). If \(F\) contained a copy of \(H\), then for each edge of that \(H\) one could choose a member of \(\mathcal S\) containing it. An inclusion-minimal such subfamily would be a hyperedge of \(\mathcal A_{H,m}(G)\) contained in \(\mathcal S\), a contradiction. Hence \(F\) is \(H\)-free and contains every member of \(\mathcal S\). Therefore
\[
\operatorname{ex}(G,K_m,H)\ge |\mathcal S|.
\]
Taking \(\mathcal S\) maximum proves the equality. \(\square\)

This exact identity is the source of the covering-density obstruction below.

---

## 3. A computable range where the proposed formula is false

For a family \(\mathcal J\) of at least two distinct copies of \(K_m\), define its relative clique density by
\[
d_m(\mathcal J)
   =\frac{e(\mathcal J)-a}{v(\mathcal J)-m}.
\]
Both numerator and denominator are positive.

For a minimal \(H\)-cover \(\mathcal C\), let
\[
D_m(\mathcal C)
   =\max_{\substack{\mathcal J\subseteq\mathcal C\\|\mathcal J|\ge2}}
      d_m(\mathcal J),
\]
and define
\[
d_{\mathrm{cov}}(H,m)
   =\min_{\mathcal C}D_m(\mathcal C),
\]
where the minimum is over all isomorphism types of minimal \(H\)-covers. This is a minimum over a finite set and is therefore a computable rational number.

### Theorem 3.1: the all-cliques phase

Suppose
\[
\mu\to\infty
\qquad\text{and}\qquad
p=o\!\left(n^{-1/d_{\mathrm{cov}}(H,m)}\right).
\]
Then, with high probability,
\[
\operatorname{ex}(G(n,p),K_m,H)
   =(1-o(1))N(K_m,G(n,p))
   =(1+o(1))\mu.
\]
In particular, the formula in the question is false in this range.

#### Proof

For each minimal covering type \(\mathcal C\), choose a subfamily
\(\mathcal J_{\mathcal C}\subseteq\mathcal C\) attaining \(D_m(\mathcal C)\).
Let
\[
\Delta v=v(\mathcal J_{\mathcal C})-m,\qquad
\Delta e=e(\mathcal J_{\mathcal C})-a.
\]
The expected number of labeled occurrences of \(\mathcal J_{\mathcal C}\) in \(G(n,p)\) is at most
\[
O\!\left(n^{v(\mathcal J_{\mathcal C})}
          p^{e(\mathcal J_{\mathcal C})}\right).
\]
Relative to \(\mu\), this is
\[
O\!\left(n^{\Delta v}p^{\Delta e}\right).
\]

Write
\[
p=n^{-1/d_{\mathrm{cov}}}\eta_n,
\qquad \eta_n\to0.
\]
Since
\[
\frac{\Delta e}{\Delta v}
 =D_m(\mathcal C)\ge d_{\mathrm{cov}},
\]
we have
\[
n^{\Delta v}p^{\Delta e}
 =\eta_n^{\Delta e}
   n^{\Delta v-\Delta e/d_{\mathrm{cov}}}
 =o(1).
\]
There are only finitely many covering types. Hence the total number \(Z\) of occurrences of all the selected subpatterns \(\mathcal J_{\mathcal C}\) satisfies
\[
Z=o(\mu)
\]
with high probability, by Markov's inequality.

Delete one \(K_m\) from every such occurrence. At most \(Z=o(\mu)\) copies are deleted. The remaining family contains no minimal \(H\)-cover: an occurrence of a covering type \(\mathcal C\) would contain the designated subpattern \(\mathcal J_{\mathcal C}\), one member of which was deleted.

By Lemma 2.1, the union of the edges of the remaining \(K_m\)'s is \(H\)-free. Thus
\[
\operatorname{ex}(G(n,p),K_m,H)
   \ge N(K_m,G(n,p))-o(\mu).
\]

Finally, when \(\mu\to\infty\),
\[
N(K_m,G(n,p))=(1+o(1))\mu
\]
with high probability. For completeness, the variance contributions from two \(K_m\)'s meeting in \(r\) vertices are, after division by \(\mu^2\),
\[
O\!\left(n^{-r}p^{-\binom r2}\right),
\qquad 2\le r\le m-1.
\]
Writing \(p=n^{-2/(m-1)}\omega_n\), where \(\omega_n\to\infty\), these are
\[
O\!\left(
n^{-r(m-r)/(m-1)}
\omega_n^{-\binom r2}
\right)=o(1).
\]
This proves concentration and hence the theorem. \(\square\)

Since the desired quantity is \((\rho+o(1))\mu\), while Theorem 3.1 gives \((1+o(1))\mu\), the ratio between the true optimum and the proposed expression tends to \(1/\rho>1\).

---

## 4. Bounds and exact computation of \(d_{\mathrm{cov}}\)

Let
\[
M=m_2(H),\qquad
D=m_2(K_m)=\frac{\binom m2-1}{m-2}=\frac{m+1}{2}.
\]

### Proposition 4.1
For every \(H\) with \(\chi(H)>m\),
\[
\frac m2\le d_{\mathrm{cov}}(H,m).
\]

#### Proof

Choose a connected component \(H_0\) of \(H\) with chromatic number \(k>m\). In any cover, choose one \(K_m\) covering each edge of \(H_0\). At least two distinct \(K_m\)'s are needed, since otherwise \(H_0\) would be a subgraph of \(K_m\).

The line graph of the connected graph \(H_0\) is connected. Hence two adjacent edges of \(H_0\) are assigned to distinct covering cliques \(Q,Q'\). These cliques meet in at least their common endpoint. Let \(r=|Q\cap Q'|\), where \(1\le r\le m-1\). Then
\[
d_m(\{Q,Q'\})
 =\frac{\binom m2-\binom r2}{m-r}
 =\frac{m+r-1}{2}
 \ge\frac m2.
\]
Thus every cover has \(D_m(\mathcal C)\ge m/2\). \(\square\)

There is also a useful explicit upper bound. Construct the **canonical cover** by extending every edge \(uv\in E(H)\) to a \(K_m\) using \(m-2\) fresh vertices, all fresh vertices being distinct for different edges.

For a subfamily indexed by an edge set \(S\subseteq E(H)\), write
\[
q=|S|,\qquad s=|V(S)|.
\]
Its members have pairwise edge-disjoint 2-shadows, so
\[
e(\mathcal J)=aq,\qquad
v(\mathcal J)=s+(m-2)q.
\]
Consequently,
\[
d_m(\mathcal J)
 =\frac{a(q-1)}
        {(s-2)+(m-2)(q-1)}.
\]
Putting
\[
r_S=\frac{q-1}{s-2},
\]
this becomes
\[
f_m(r_S)
 :=\frac{a r_S}{1+(m-2)r_S}.
\]
The function \(f_m\) is increasing, and
\[
\max_{S\subseteq E(H)}r_S=m_2(H)=M.
\]
Therefore the canonical cover satisfies
\[
D_m(\mathcal C_{\mathrm{can}})
 =f_m(M)
 =\frac{\binom m2\,M}{1+(m-2)M}.
\]

We obtain:

### Corollary 4.2
\[
\boxed{
\frac m2
 \le d_{\mathrm{cov}}(H,m)
 \le \frac{\binom m2\,m_2(H)}
          {1+(m-2)m_2(H)}.
}
\]

In the hard regime \(M<D\),
\[
f_m(M)<f_m(D)=D,
\]
so
\[
d_{\mathrm{cov}}(H,m)<m_2(K_m).
\]

For \(m=3\), this reads
\[
\frac32\le d_{\mathrm{cov}}(H,3)
 \le \frac{3m_2(H)}{1+m_2(H)}<2.
\]

### Exact finite algorithm

Let \(h=v(H)\) and \(e=e(H)\), after deleting isolated vertices. To compute \(d_{\mathrm{cov}}(H,m)\):

1. For each \(q=2,\dots,e\), set
   \[
   N_{\max}=h+(m-2)q.
   \]
2. For each \(N\in[h,N_{\max}]\), enumerate families
   \[
   \mathcal C=\{Q_1,\dots,Q_q\}\subseteq\binom{[N]}m
   \]
   with \(V(\mathcal C)=[N]\).
3. Regard \(H\) as fixed on \([h]\), and retain precisely those families satisfying:
   - every edge \(uv\in E(H)\) is contained in some \(Q_i\);
   - for every \(i\), there is an edge \(uv\in E(H)\) contained in \(Q_i\) and in no \(Q_j\) with \(j\ne i\).
4. For every retained family compute
   \[
   D_m(\mathcal C)
    =\max_{\substack{\mathcal J\subseteq\mathcal C\\|\mathcal J|\ge2}}
       \frac{e(\mathcal J)-a}{v(\mathcal J)-m}.
   \]
5. Return the minimum.

This terminates and uses exact rational arithmetic. It is not computationally efficient, but it fully specifies the finite parameter.

---

## 5. A sharper deterministic Turán reduction

The preceding parameter only detects the phase where almost every \(K_m\) can be retained. One can isolate the remaining obstruction more precisely.

For \(x>0\), let
\[
\mathfrak C_{<x}
 =\{\mathcal C:\mathcal C\text{ is a minimal }H\text{-cover and }
                 D_m(\mathcal C)<x\}.
\]
Regard each \(\mathcal C\) as a finite \(m\)-uniform hypergraph whose hyperedges are its \(m\)-sets.

Let
\[
\operatorname{ex}^{(m)}(N,\mathfrak C_{<x})
\]
be the largest size of a family
\(\mathcal S\subseteq\binom{[N]}m\) containing no copy of any member of
\(\mathfrak C_{<x}\), and define
\[
\Pi(x)
 =\lim_{N\to\infty}
   \frac{\operatorname{ex}^{(m)}(N,\mathfrak C_{<x})}{\binom Nm}.
\]
The limit exists by the usual averaging over \((N-1)\)-vertex restrictions.

The function \(\Pi(x)\) is nonincreasing and takes only finitely many values as \(x\) crosses the finitely many numbers \(D_m(\mathcal C)\). Moreover,
\[
\Pi(x)=1\qquad\text{for }x\le d_{\mathrm{cov}}(H,m).
\]

If all minimal coverings are forbidden, a family \(\mathcal S\) is allowed exactly when its 2-shadow is \(H\)-free. Lemma 2.1 with \(G=K_N\) therefore gives
\[
\lim_{x\to\infty}\Pi(x)
 =\lim_{N\to\infty}
   \frac{\operatorname{ex}(N,K_m,H)}{\binom Nm}
 =\rho.
\]

The following gives a rigorous lower obstruction at every intermediate stage.

### Proposition 5.1
Fix \(x>0\). If
\[
\mu\to\infty
\qquad\text{and}\qquad
p=o(n^{-1/x}),
\]
then with high probability
\[
\operatorname{ex}(G(n,p),K_m,H)
 \ge (\Pi(x)-o(1))\mu.
\]
Consequently, if \(\Pi(x)>\rho\), the formula in the question is false in this range.

#### Proof

Choose a deterministic family
\[
\mathcal S_n\subseteq\binom{[n]}m
\]
that avoids every configuration in \(\mathfrak C_{<x}\) and has
\[
|\mathcal S_n|=(\Pi(x)+o(1))\binom nm.
\]
Let \(\mathcal S_n(p)\) be the members of \(\mathcal S_n\) that span copies of \(K_m\) in \(G(n,p)\).

The same variance calculation as for the full clique count gives
\[
|\mathcal S_n(p)|=(\Pi(x)+o(1))\mu
\]
with high probability.

For every covering type \(\mathcal C\) with \(D_m(\mathcal C)\ge x\), select a subfamily \(\mathcal J_{\mathcal C}\) attaining \(D_m(\mathcal C)\). If
\[
\Delta v=v(\mathcal J_{\mathcal C})-m,\qquad
\Delta e=e(\mathcal J_{\mathcal C})-a,
\]
then
\[
\frac{\Delta e}{\Delta v}\ge x.
\]
Since \(p=o(n^{-1/x})\),
\[
n^{\Delta v}p^{\Delta e}=o(1).
\]
Thus the total number of occurrences of all these selected subpatterns is \(o(\mu)\) with high probability.

Delete one member of \(\mathcal S_n(p)\) from each such occurrence. The resulting family:

- contains no cover \(\mathcal C\) with \(D_m(\mathcal C)<x\), because it is a subfamily of \(\mathcal S_n\);
- contains no cover with \(D_m(\mathcal C)\ge x\), because its selected dense subpattern was hit.

It therefore contains no \(H\)-cover at all. Its edge-union is \(H\)-free and contains at least
\[
(\Pi(x)-o(1))\mu
\]
copies of \(K_m\). \(\square\)

This identifies a finite collection of deterministic hypergraph Turán problems controlling lower bounds for the random transition.

One may define
\[
d_{\mathrm{Tur}}
 =\sup\{x:\Pi(x)>\rho\}.
\]
Then
\[
d_{\mathrm{cov}}(H,m)\le d_{\mathrm{Tur}}.
\]
Proposition 5.1 proves failure of the desired formula below every scale
\(n^{-1/x}\) for which \(\Pi(x)>\rho\).

For \(m=2\), there is only one covering: the edge set of \(H\). Its density is \(m_2(H)\), and \(\Pi(x)\) jumps directly from \(1\) to \(1-1/(k-1)\). This recovers the structural reason why the edge problem has a single \(m_2(H)\)-threshold. For \(m\ge3\), several nonisomorphic clique coverings can intervene, and the intermediate values of \(\Pi(x)\) are genuine hypergraph Turán questions.

---

## 6. Consequences for the catalog question

Let
\[
M=m_2(H),\qquad D=m_2(K_m)=\frac{m+1}{2}.
\]

The source paper, as summarized in the question, gives the desired formula in the hard regime at least when
\[
p\gg n^{-1/D}=n^{-2/(m+1)}.
\]
Combining that quoted result with Proposition 5.1 implies
\[
d_{\mathrm{Tur}}\le D.
\]
Indeed, if \(\Pi(x)>\rho\) for some \(x>D\), choose
\[
\frac1x<\alpha<\frac1D,\qquad p=n^{-\alpha}.
\]
Then Proposition 5.1 says the formula fails, whereas the quoted high-density theorem says it holds.

Thus the presently justified picture is
\[
\boxed{
\frac m2
 \le d_{\mathrm{cov}}(H,m)
 \le d_{\mathrm{Tur}}
 \le m_2(K_m),
}
\]
with
\[
d_{\mathrm{cov}}(H,m)
 \le \frac{\binom m2\,m_2(H)}
          {1+(m-2)m_2(H)}
 <m_2(K_m)
\]
in the hard regime.

In particular:

- if \(p\ll n^{-1/d_{\mathrm{cov}}(H,m)}\) and \(\mu\to\infty\), then almost all \(K_m\)'s can be retained and the proposed formula is false;
- more generally, if \(\Pi(x)>\rho\) and \(p\ll n^{-1/x}\), then the proposed formula is false;
- the supplied source gives the formula for \(p\gg n^{-1/m_2(K_m)}\);
- the exact onset between these scales remains unresolved.

For example, when \(m=3\) and \(k=4\), the target proportion is
\[
\rho=\frac{6}{27}=\frac29.
\]
Below the all-cliques threshold from Theorem 3.1, the optimum is asymptotic to all triangles, rather than \(2/9\) of them.

---

## 7. Remaining gap

There are two distinct unresolved steps.

1. **Deterministic covering Turán densities.**  
   One must determine when
   \[
   \Pi(x)=\rho.
   \]
   This is a finite forbidden \(m\)-uniform hypergraph Turán problem, but such densities are generally difficult and need not be determined by \(m_2(H)\) alone.

2. **Sparse upper transference.**  
   Even if \(\Pi(x)=\rho\), one still needs to prove that every \(H\)-free subgraph of \(G(n,p)\) has at most \((\rho+o(1))\mu\) copies of \(K_m\) when \(p\gg n^{-1/x}\). The available copies of \(K_m\) are not sampled independently: they are generated by common random graph edges. The required sparse supersaturation statement is exactly the missing high-side argument.

No claim is made at critical scales \(p=\Theta(n^{-1/x})\), where constant factors or logarithmic corrections may matter.

The catalog reports that Samotij and Shikhelman develop a covering-density reduction of this kind. I therefore regard the results above as a self-contained verification and sharpening of the obstruction mechanism, not as a resolution or a novelty claim suitable for publication.