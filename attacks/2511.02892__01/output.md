```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The a.a.s. question remains unresolved, but the coefficient is exactly a signed count of proper 3-colourings, yielding cancellation criteria, an infinite family of 3-colourable zero examples, and an exact configuration-model second moment.",
  "would_publish": false,
  "caveats": "No anti-concentration estimate is obtained for the uniform simple 4-regular model, and the explicit zero family is highly non-random."
}
```

# Mathematical writeup

## 1. Statement and conventions

Let \(G\) be a loopless 4-regular graph on \(N\) vertices. Choose an arbitrary orientation \(\vec E\) of its edges and write

\[
P_{\vec G}(x)=\prod_{(u,v)\in \vec E}(x_u-x_v),
\qquad
c_{\vec G}=[\prod_{v\in V(G)}x_v^2]P_{\vec G}(x).
\]

Reversing one chosen edge orientation multiplies \(P_{\vec G}\), and hence \(c_{\vec G}\), by \(-1\). Thus the assertion \(c_{\vec G}\neq0\) is independent of these choices.

I interpret “random 4-regular graph” as the uniformly random labelled simple 4-regular graph. For the unconditioned configuration multigraph model, the assertion is false as stated: loops occur with probability bounded away from zero, and a loop contributes a factor \(x_v-x_v=0\).

The main probabilistic question for simple graphs remains open here.

---

## 2. An exact signed 3-colouring formula

Let \(\omega=e^{2\pi i/3}\). For a proper colouring
\(\phi:V(G)\to\{0,1,2\}\), put \(z_v=\omega^{\phi(v)}\) and define

\[
\varepsilon_{\vec G}(\phi)
 =
3^{-N}
\left(\prod_{v\in V(G)}z_v\right)
\prod_{(u,v)\in\vec E}(z_u-z_v).
\]

### Theorem 2.1

For every loopless 4-regular graph,

\[
\boxed{\displaystyle
c_{\vec G}=\sum_{\phi\in\operatorname{Col}_3(G)}
\varepsilon_{\vec G}(\phi),
}
\]

and every summand satisfies

\[
\varepsilon_{\vec G}(\phi)\in\{+1,-1\}.
\]

Moreover, globally permuting the three colours does not change
\(\varepsilon_{\vec G}(\phi)\).

### Proof

For a one-variable polynomial \(f\) of degree at most \(4\),

\[
[x^2]f(x)=\frac13\sum_{z\in\{1,\omega,\omega^2\}}z^{-2}f(z),
\]

because the right-hand side retains precisely powers congruent to \(2\pmod 3\), and among \(0,1,2,3,4\) only the exponent \(2\) has this residue.

Applying this independently at every vertex gives

\[
c_{\vec G}
 =
3^{-N}\sum_{z_v\in\{1,\omega,\omega^2\}}
\left(\prod_v z_v^{-2}\right)
P_{\vec G}(z).
\]

Since \(z^{-2}=z\) for a cube root of unity, this is the claimed expression. Any assignment giving equal values to adjacent vertices contributes zero, so only proper 3-colourings remain.

For distinct cube roots \(z,w\),

\[
(z-w)^2=-3zw.
\]

Because \(|E(G)|=2N\) and every vertex has degree \(4\),

\[
\begin{aligned}
\varepsilon_{\vec G}(\phi)^2
&=
3^{-2N}
\left(\prod_v z_v^2\right)
\prod_{uv\in E(G)}(z_u-z_v)^2\\
&=
3^{-2N}(-3)^{2N}
\left(\prod_v z_v^2\right)
\left(\prod_{uv\in E(G)}z_uz_v\right)\\
&=
\prod_v z_v^{2+4}
=1.
\end{aligned}
\]

Thus every summand is \(+1\) or \(-1\).

Adding a constant modulo \(3\) to all colours multiplies the vertex factor by \(\omega^N\) and the edge product by \(\omega^{2N}\), hence changes nothing. Reflecting the colour triangle complex-conjugates the summand, which also changes nothing because it is real. These operations generate \(S_3\). ∎

### Consequences

1. If \(G\) is not 3-colourable, then \(c_{\vec G}=0\).

2. The action of \(S_3\) on proper colourings is free for a nonempty graph, and each orbit has constant sign. Hence

   \[
   6\mid c_{\vec G}.
   \]

3. If \(\operatorname{col}_3(G)\) denotes the number of proper labelled 3-colourings, then

   \[
   \boxed{\displaystyle
   c_{\vec G}\equiv \operatorname{col}_3(G)\pmod {12}.
   }
   \]

   Indeed, every colour orbit contributes either \(+6\) or \(-6\), both congruent to \(6\pmod{12}\).

4. In particular, if the number of proper 3-colourings modulo colour permutation is odd, then \(c_{\vec G}\neq0\). Uniquely 3-colourable graphs satisfy \(c_{\vec G}=\pm6\).

These criteria do not appear likely to hold a.a.s. for random 4-regular graphs, but they give exact deterministic certificates.

---

## 3. A useful explicit sign formula

Orient the colour triangle cyclically as

\[
0\longrightarrow1\longrightarrow2\longrightarrow0.
\]

For a proper colouring \(\phi\), let \(q_{\vec G}(\phi)\) be the number of oriented graph edges \((u,v)\in\vec E\) for which the colour transition
\(\phi(u)\to\phi(v)\) goes opposite to this cyclic orientation.

### Proposition 3.1

\[
\boxed{\displaystyle
\varepsilon_{\vec G}(\phi)=(-1)^{N+q_{\vec G}(\phi)}.
}
\]

### Proof

Set \(A=1-\omega\). If an oriented edge follows the cyclic colour orientation, then

\[
\omega^{\phi(u)}-\omega^{\phi(v)}
=A\omega^a,
\]

where \(a\) is the cyclic predecessor colour on that edge. If it goes oppositely, there is an additional minus sign.

Let \(n_i\) be the number of vertices of colour \(i\), and let \(e_{ij}\) be the number of edges joining colours \(i,j\). The phase left after extracting \((-1)^{q_{\vec G}(\phi)}A^{2N}\) is

\[
\omega^{N+n_1+2n_2+e_{12}+2e_{20}},
\]

because \(A^{2N}=(-3\omega)^N\).

The degree equations are

\[
e_{01}+e_{20}=4n_0,\quad
e_{01}+e_{12}=4n_1,\quad
e_{12}+e_{20}=4n_2.
\]

Modulo \(3\), these imply

\[
e_{20}\equiv n_0-e_{01},
\qquad
e_{12}\equiv n_1-e_{01}.
\]

Consequently,

\[
N+n_1+2n_2+e_{12}+2e_{20}
\equiv N+2(n_0+n_1+n_2)-3e_{01}
\equiv0\pmod3.
\]

Thus the phase is \(1\), giving the formula. ∎

---

## 4. Kempe-component cancellation

Let \(S\) be a connected component of the subgraph induced by two colours in a proper 3-colouring. Swap those two colours on \(S\).

### Proposition 4.1

The sign of the colouring is multiplied by

\[
\boxed{\displaystyle (-1)^{|E(G[S])|}.}
\]

### Proof

Relabel the two colours as \(0,1\). Swapping them reverses the cyclic status of every edge internal to \(S\) and every edge between \(S\) and the third colour. If \(e=|E(G[S])|\) and \(\delta=|\delta_G(S)|\), the parity change in \(q_{\vec G}\) is \(e+\delta\). Since \(G\) is 4-regular,

\[
4|S|=2e+\delta,
\]

and hence

\[
e+\delta=4|S|-e\equiv e\pmod2.
\]

The result follows from Proposition 3.1. ∎

This gives a more compressed expression for the coefficient. Let \(\mathcal I\) be the collection of independent sets \(I\subseteq V(G)\) for which \(G-I\) is bipartite. Regard \(I\) as the colour-2 class. Each component of \(G-I\) has two possible 2-colourings.

If one component \(K\) has an odd number of edges, its two possible colourings contribute opposite signs and cancel. If every component has an even number of edges, all \(2^{\kappa(G-I)}\) extensions have the same sign. Therefore

\[
\boxed{\displaystyle
c_{\vec G}
=
\sum_{\substack{
I\in\mathcal I\\
|E(K)|\ \mathrm{even\ for\ every\ component}\ K\subseteq G-I
}}
\eta_{\vec G}(I)\,2^{\kappa(G-I)},
}
\]

where \(\eta_{\vec G}(I)\in\{\pm1\}\) is the sign of any one extension.

Thus a sufficient deterministic condition for \(c_{\vec G}=0\) is:

> For every independent set \(I\) such that \(G-I\) is bipartite, some component of \(G-I\) has an odd number of edges.

This formulation isolates one source of exact cancellation that an anti-concentration proof must overcome.

---

## 5. A positive special case: bipartite graphs

### Proposition 5.1

Every 4-regular bipartite graph has nonzero central coefficient.

### Proof

Let \(V(G)=A\cup B\) be a bipartition and orient every factor as

\[
x_a-x_b,\qquad a\in A,\ b\in B.
\]

A term contributing to \(\prod_vx_v^2\) chooses exactly two incident edge factors at every vertex. Its sign is

\[
(-1)^{\text{number of chosen endpoints in }B}
=(-1)^{2|B|}=1.
\]

There is at least one such choice: orient every Eulerian component so that every vertex has indegree \(2\), and choose the head endpoint of each edge. Hence all contributing terms have the same sign and at least one exists. ∎

This gives a complete deterministic subclass, though random simple 4-regular graphs are bipartite with exponentially small probability.

---

## 6. An infinite family of 3-colourable graphs with zero coefficient

The coefficient is not merely detecting 3-colourability.

Let

\[
R_t=C_t\square K_3,\qquad t\ge3.
\]

This is a connected simple 4-regular graph on \(3t\) vertices.

### Theorem 6.1

For a suitable fixed orientation,

\[
\boxed{
c(R_t)=
\begin{cases}
0,&t\text{ odd},\\[2mm]
4(-1)^{t/2}3^{t/2},&t\text{ even}.
\end{cases}}
\]

In particular, \(C_t\square K_3\) is 3-colourable but has zero coefficient whenever \(t\) is odd.

### Proof

Index vertices by \((i,j)\in\mathbb Z_t\times\mathbb Z_3\). Orient the \(C_t\)-edges forward in the first coordinate and each \(K_3=C_3\) cyclically in the second coordinate.

In every proper 3-colouring, each \(K_3\)-fibre uses all three colours. Write its colouring as a permutation

\[
\pi_i:\mathbb Z_3\to\mathbb Z_3.
\]

The horizontal condition says that
\(\pi_{i+1}\pi_i^{-1}\) is a derangement of three symbols, hence one of the two 3-cycles. Thus

\[
\pi_{i+1}=r^{s_i}\pi_i,\qquad s_i\in\{+1,-1\},
\]

where \(r\) is the cyclic colour permutation. Closure around \(C_t\) requires

\[
\sum_{i=0}^{t-1}s_i\equiv0\pmod3.
\]

Let \(k\) be the number of indices with \(s_i=-1\), and let \(p\in\{0,1\}\) be the parity of \(\pi_0\). Multiplication by \(r\) preserves permutation parity, so all \(\pi_i\) have parity \(p\).

If \(p=0\), all three oriented edges inside each \(K_3\)-fibre follow the cyclic colour direction; if \(p=1\), all three go oppositely. Likewise, a horizontal transition with \(s_i=-1\) contributes three oppositely directed edges. Consequently,

\[
q_{\vec R_t}(\phi)\equiv pt+k\pmod2.
\]

Since \(|V(R_t)|=3t\), Proposition 3.1 gives

\[
\varepsilon(\phi)=(-1)^{t+pt+k}.
\]

There are three choices of \(\pi_0\) of each parity. Therefore

\[
c(R_t)
=
3(1+(-1)^t)
\sum_{\substack{s_i\in\{\pm1\}\\ \sum s_i\equiv0\pmod3}}
(-1)^k.
\]

The remaining sum is evaluated by a roots-of-unity filter:

\[
\begin{aligned}
S_t
&=
\sum_{\substack{s_i\in\{\pm1\}\\ \sum s_i\equiv0\pmod3}}
(-1)^k\\
&=
\frac13\left((\omega-\omega^{-1})^t+
(\omega^2-\omega^{-2})^t\right)\\
&=
\frac13\left((i\sqrt3)^t+(-i\sqrt3)^t\right).
\end{aligned}
\]

Thus \(S_t=0\) for odd \(t\), while for even \(t\),

\[
S_t=2(-1)^{t/2}3^{t/2-1}.
\]

Substitution gives the asserted formula. ∎

For comparison, the number of proper labelled 3-colourings is

\[
2\bigl(2^t+2(-1)^t\bigr),
\]

which is positive for every \(t\ge3\).

There is also a short symmetry explanation for the odd case. Reflecting the \(K_3\)-coordinate reverses all \(3t\) oriented \(K_3\)-edges and preserves the horizontal orientations. Hence it sends the polynomial to \((-1)^{3t}P=(-1)^tP\), while fixing the central monomial. For odd \(t\), its coefficient must therefore vanish.

---

## 7. Exact second moment in the pairing model

Although this does not settle the simple-graph problem, the second moment can be calculated exactly in the configuration model.

Give each of \(N\) vertices four distinguishable stubs, and let \(M\) be a uniformly random perfect matching of the \(4N\) stubs. Orient every matched pair from its lower-numbered stub to its higher-numbered stub, and let \(C(M)\) be the central coefficient of the resulting pairing polynomial. Its square is independent of the orientation convention.

### Theorem 7.1

\[
\boxed{\displaystyle
\mathbb E\,C(M)^2
=
\frac{6^N(2N+1)!}{(4N-1)!!}
\int_0^1(1-6x+6x^2)^N\,dx.
}
\]

Moreover,

\[
\boxed{\displaystyle
\mathbb E\,C(M)^2
\sim
\frac23\sqrt{2\pi N}\left(\frac32\right)^N.
}
\]

### Proof

A term of the central coefficient can be encoded by a subset \(S\) of the stubs containing exactly two stubs at each vertex. It contributes only if every matched pair has exactly one endpoint in \(S\). Its sign records whether the lower or upper endpoint was selected.

For two such subsets \(S,T\), divide the stubs into

\[
A=S\cap T,\quad
B=S\setminus T,\quad
C=T\setminus S,\quad
D=\overline{S\cup T}.
\]

A matching crosses both \(S\) and \(T\) precisely when it pairs \(A\) with \(D\) and \(B\) with \(C\). Since \(|S|=|T|=2N\),

\[
|A|=|D|=:a,\qquad |B|=|C|=:b=2N-a.
\]

There are \(a!b!\) such matchings. The product of the two term signs is \(+1\) on every \(A\)-\(D\) edge and \(-1\) on every \(B\)-\(C\) edge, giving total sign

\[
(-1)^b=(-1)^a.
\]

For a fixed local choice of \(S\) at one vertex, the number of choices of \(T\) with intersection size \(0,1,2\) is respectively \(1,4,1\). Hence the number of ordered pairs \((S,T)\) with total intersection size \(a\) is

\[
6^N[z^a](1+4z+z^2)^N.
\]

It follows that

\[
\mathbb E C(M)^2
=
\frac{6^N}{(4N-1)!!}
\sum_{a=0}^{2N}
[z^a](1+4z+z^2)^N(-1)^a a!(2N-a)!.
\]

Using

\[
a!(2N-a)!
=
(2N+1)!\int_0^1x^a(1-x)^{2N-a}\,dx,
\]

the sum inside the integral becomes

\[
\begin{aligned}
&(1-x)^{2N}
\left(
1-\frac{4x}{1-x}+\frac{x^2}{(1-x)^2}
\right)^N\\
&\hspace{25mm}=(1-6x+6x^2)^N,
\end{aligned}
\]

proving the exact formula.

The polynomial \(1-6x+6x^2\) attains absolute maximum \(1\) only at \(x=0,1\), and near either endpoint it is \(1-6x+O(x^2)\). Thus

\[
\int_0^1(1-6x+6x^2)^N\,dx\sim\frac1{3N}.
\]

Finally,

\[
(4N-1)!!=\frac{(4N)!}{2^{2N}(2N)!},
\qquad
\binom{4N}{2N}\sim\frac{16^N}{\sqrt{2\pi N}},
\]

which yields the asymptotic formula. ∎

If \(B(M)\) denotes the unsigned number of balanced endpoint selections, then similarly

\[
\mathbb E B(M)
=
\frac{6^N(2N)!}{(4N-1)!!}
\sim
\sqrt{2\pi N}\left(\frac32\right)^N,
\]

and hence

\[
\frac{\mathbb E C(M)^2}{\mathbb E B(M)}\longrightarrow\frac23.
\]

This gives a natural scale for the signed coefficient. It does not control the atom at zero. In particular, neither this second moment nor its positivity prevents the second moment from being supported on a small set of pairings with unusually large coefficients. Conditioning on simplicity is also a weighted conditioning and cannot be justified from the displayed formula alone.

---

## 8. Reproducible exact computation

Proposition 3.1 gives a direct integer algorithm avoiding symbolic polynomial expansion:

```python
from itertools import product

def central_coefficient(n, oriented_edges):
    # oriented_edges contains one ordered pair (u,v) per edge,
    # corresponding to the factor x_u - x_v.
    ans = 0
    for phi in product(range(3), repeat=n):
        if any(phi[u] == phi[v] for u, v in oriented_edges):
            continue
        q = sum(((phi[v] - phi[u]) % 3) == 2
                for u, v in oriented_edges)
        ans += -1 if ((n + q) % 2) else 1
    return ans
```

For a 4-regular input this returns the exact coefficient. Reversing one ordered edge changes the returned value by an overall minus sign, as expected.

---

## 9. Remaining gap

For the intended uniformly random simple 4-regular graph, one still needs to prove

\[
\Pr(c_{\vec G}=0)\longrightarrow0.
\]

The signed-colouring identity shows that this is an exact anti-concentration problem for a highly dependent \(\{\pm1\}\)-sum. The family \(C_t\square K_3\) demonstrates that complete cancellation can occur even in connected, simple, 3-colourable 4-regular graphs. The exact configuration-model second moment quantifies the expected scale but gives no bound on the zero atom.

Thus neither a proof nor an asymptotically relevant counterexample is obtained. The main unresolved step remains an anti-concentration or local-limit estimate robust under conditioning on simplicity.