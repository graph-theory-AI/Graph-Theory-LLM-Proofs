```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but fixed blow-ups preserve exponential upper bounds and the natural five-vertex candidate \(C_5^{(3)-}\) satisfies the explicit recurrence \(R(n)\le Cn^4R(n-2)\), while the required \(2^{O(n)}\) improvement remains missing.",
  "would_publish": false,
  "caveats": "The prompt omits the source candidate's edge set, so I do not identify it definitively with \(C_5^{(3)-}\); no purely exponential upper bound is proved."
}
```

# 1. Statement and notation

For a fixed 3-uniform hypergraph \(H\), write
\[
R_H(n)=r(H,K_n^{(3)}).
\]
Equivalently, \(R_H(n)\) is the least \(N\) such that every \(H\)-free 3-graph on \(N\) vertices has an independent set of order \(n\).

I do not prove or disprove the conjecture. I give:

1. a quantitative blow-up transfer lemma which reduces the search to strong homomorphic cores;
2. a pair-neighborhood operation preserving exponential upper bounds;
3. a classification showing that, among 3-graphs on at most five vertices, the only possible purely exponential example is \(C_5^{(3)-}\);
4. for that graph, an explicit recurrence
   \[
   R_H(n)\le Cn^4R_H(n-2),
   \]
   yielding \(2^{O(n\log n)}\) and identifying exactly where this method loses the unwanted \(\log n\).

No result from the unverified 2025 follow-up is used.

# 2. Fixed blow-ups only change the logarithm of the Ramsey number by a constant factor

For a 3-graph \(F\) and integer \(s\ge 1\), let \(F(s)\) be its complete \(s\)-blow-up: every \(v\in V(F)\) is replaced by a class \(V_v\) of size \(s\), and for each \(abc\in E(F)\), all triples with one vertex in each of \(V_a,V_b,V_c\) are edges.

## Proposition 2.1

For every fixed 3-graph \(F\) and fixed \(s\), there is a constant \(C=C(F,s)\) such that
\[
R_{F(s)}(n)\le R_F(n)^C.
\]

Consequently, if a fixed 3-graph \(H\) is a subgraph of \(F(s)\), then
\[
R_H(n)\le R_F(n)^C.
\]

### Proof

Put \(f=v(F)\) and \(R=R_F(n)\). Let \(G\) be a red 3-graph on \(N\) vertices with no independent \(n\)-set. Every \(R\)-vertex subset of \(V(G)\) contains a red copy of \(F\).

Counting pairs consisting of an \(R\)-set and a copy of \(F\) contained in it shows that the number of \(f\)-vertex supports of red copies of \(F\) is at least
\[
\frac{\binom NR}{\binom{N-f}{R-f}}
 =\frac{\binom Nf}{\binom Rf}
 \ge c_F\left(\frac NR\right)^f.
\]
Choose one labeled embedding on each such support. Randomly partition \(V(G)\) into \(f\) ordered parts, one for each vertex of \(F\). Some partition retains at least
\[
c'_F R^{-f}N^f
\]
of these labeled copies with every label in its prescribed part.

We use the following standard fixed-parameter extraction fact.

### Multipartite extraction lemma

For fixed \(q,s\), there is \(C_0=C_0(q,s)\) such that any \(q\)-partite \(q\)-uniform hypergraph with at least \(\delta N^q\) edges contains a complete \(q\)-partite \(q\)-graph with \(s\) vertices in each part, provided
\[
N\ge \delta^{-C_0}.
\]

For completeness, this follows by induction on \(q\). For a \((q-1)\)-tuple \(x\), let \(d(x)\) be its degree into the last part. Double-counting pairs \((x,S)\) with \(S\in\binom{N(x)}s\), followed by convexity, gives an \(s\)-set in the last part with at least
\[
c_{q,s}\delta^s N^{q-1}
\]
common \((q-1)\)-tuples. Apply induction to this common \((q-1)\)-graph. All losses are fixed powers of \(\delta\).

Apply the lemma to the \(f\)-partite auxiliary \(f\)-graph whose edges are the retained labeled copies of \(F\). Here \(\delta=c'_F R^{-f}\). Thus \(N\ge R^C\), for a sufficiently large \(C=C(F,s)\), gives classes \(U_v\), \(v\in V(F)\), each of size \(s\), such that every transversal choice is a labeled red copy of \(F\). In particular, for every \(abc\in E(F)\), every triple in \(U_a\times U_b\times U_c\) is red. This is a red \(F(s)\). ∎

## Strong-homomorphism consequence

Call \(\phi:V(H)\to V(F)\) a strong homomorphism if, for every \(xyz\in E(H)\), the three images are distinct and
\[
\phi(x)\phi(y)\phi(z)\in E(F).
\]
Such a map embeds \(H\) into \(F(s)\), where \(s\) is the maximum fiber size. Hence:

## Corollary 2.2

If \(H\) admits a strong homomorphism to \(F\), then
\[
R_H(n)\le R_F(n)^{C_{H,F}}.
\]

In particular:

- if \(R_F(n)\le 2^{O(n)}\), the same holds for \(H\);
- if \(R_H(n)\ge 2^{\Omega(n)}\), then necessarily
  \[
  R_F(n)\ge 2^{\Omega(n)}.
  \]

This gives a finite diagnostic for the source paper's explicit candidate once its edge set is supplied: enumerate its strong quotients and check whether one lies in a class with a known \(2^{O(n)}\) upper bound.

# 3. Pair-neighborhood suspension

For a fixed 3-graph \(F\), define \(\Sigma_2(F)\) by adjoining two new vertices \(a,b\) and all edges
\[
abx,\qquad x\in V(F),
\]
while retaining all edges of \(F\).

## Proposition 3.1

For every fixed \(F\),
\[
R_F(n)\le R_{\Sigma_2(F)}(n)\le C_F n^2 R_F(n).
\]

### Proof

The lower bound follows from \(F\subseteq\Sigma_2(F)\).

Let \(G\) be \(\Sigma_2(F)\)-free with \(\alpha(G)<n\), and put \(R=R_F(n)\). For a pair \(xy\), let
\[
N_G(xy)=\{z\notin\{x,y\}:xyz\in E(G)\}.
\]
If \(|N_G(xy)|\ge R\), then \(G[N_G(xy)]\), being \(F\)-free only if no copy extends \(xy\), must contain either a copy of \(F\) or an independent \(n\)-set. The latter is excluded. A copy of \(F\) inside \(N_G(xy)\), together with \(x,y\), gives \(\Sigma_2(F)\), also excluded. Therefore
\[
\Delta_2(G)<R.
\]
Consequently,
\[
e(G)\le \frac{\Delta_2(G)}3\binom{|V(G)|}{2}
       \le \frac{R|V(G)|^2}{6}.
\]

For any 3-graph with \(N\) vertices and \(E\) edges, random sampling followed by deleting one vertex from every surviving edge gives
\[
\alpha(G)\ge c\min\left\{N,\frac{N^{3/2}}{\sqrt E}\right\}.
\]
Thus here
\[
\alpha(G)\ge c\sqrt{\frac NR}.
\]
If \(N\ge C_Fn^2R\), this is at least \(n\), a contradiction. ∎

Thus this natural operation cannot by itself create a polynomial-to-exponential transition.

# 4. The five-vertex boundary

Define
\[
F=C_5^{(3)-}
\]
on vertices \(\{1,2,3,4,5\}\) with edges
\[
E(F)=\{123,124,135,245\}. \tag{4.1}
\]
Adding the edge \(345\) gives a tight 5-cycle: in cyclic order
\[
5,3,1,2,4
\]
the five consecutive triples are
\[
135,123,124,245,345.
\]

The 2-shadow of \(F\) has nine pairs—it is \(K_5\) minus the pair \(34\). Therefore, under the convention
\[
m_{\rm pair}(J)=\max_{\varnothing\ne J'\subseteq J}
\frac{e(J')}{|\partial_2J'|},
\]
one obtains
\[
m_{\rm pair}(F)=\frac49.
\]
Indeed, the relevant smaller ratios are \(1/3\), \(2/5\), and \(3/7\).

## Proposition 4.1

Let \(H\) be a nonempty 3-graph on at most five vertices. Using the \(2^{\Omega(n\log n)}\) lower bounds quoted in the question for \(K_4^{(3)-}\) and the tight 5-cycle, if
\[
R_H(n)=2^{\Theta(n)},
\]
then necessarily
\[
H\cong C_5^{(3)-},
\]
up to isolated vertices.

### Proof

Isolated vertices change \(R_H(n)\) by at most an additive constant, so discard them.

If \(H\) contains \(K_4^{(3)-}\), then
\[
R_H(n)\ge R_{K_4^{(3)-}}(n)=2^{\Omega(n\log n)},
\]
so \(H\) cannot have purely exponential growth. We may therefore assume that every four vertices span at most two edges.

If every pair of vertices has codegree at most one, then \(H\) has at most two edges. Indeed, three linear triples have union of size at least six. Every 3-graph with at most two edges is 3-partite. A fixed 3-partite 3-graph is contained in a fixed blow-up of one edge, so Proposition 2.1 gives a polynomial Ramsey number.

We may now choose a pair, say \(12\), with at least two neighbors. Relabel so that \(123,124\in E(H)\).

### Case 1: \(d_H(12)=3\)

Then \(125\in E(H)\). Any further edge involving \(1\) or \(2\), other than these three, creates three edges on some four vertices. The only remaining possible edge is \(345\). Hence
\[
H\subseteq S:=\{123,124,125,345\}.
\]
This \(S\) is \(\Sigma_2(E_3)\), where \(E_3\) is a single 3-edge. Proposition 3.1 gives
\[
R_S(n)=O(n^3).
\]

### Case 2: \(d_H(12)=2\)

Thus \(125\notin E(H)\). The edges \(134,234\) are forbidden because either would create three edges on \(\{1,2,3,4\}\). The remaining possibilities are
\[
A=135,\quad B=145,\quad C=235,\quad D=245,\quad E=345.
\]

The condition that no four vertices span three edges gives:

- \(A\) and \(C\) cannot both occur;
- \(B\) and \(D\) cannot both occur;
- if \(E\) occurs, then neither \(A,B\) nor \(C,D\) can both occur.

If \(E\) is absent, the only non-3-partite maximal choices are
\[
\{A,D\}\quad\text{or}\quad\{B,C\},
\]
and both give the graph \(F\) in (4.1).

If \(E\) is present, at most two of \(A,B,C,D\) occur. A single one, together with \(123,124,E\), is again isomorphic to \(F\); for example
\[
\{123,124,135,345\}
\]
is the four-edge tight path with cyclic sequence \(4,2,1,3,5,4\). If the two allowed edges \(A,D\) occur, or symmetrically \(B,C\), all five edges form the tight 5-cycle. With none of \(A,B,C,D\), the hypergraph is a subgraph of \(S\).

Thus every case is one of:

- a fixed 3-partite 3-graph, hence polynomial;
- a subgraph of \(S\), hence polynomial;
- \(F=C_5^{(3)-}\);
- the full tight \(C_5^{(3)}\), which has the quoted \(2^{\Omega(n\log n)}\) lower bound.

This proves the assertion. ∎

This does not prove that \(F\) has an exponential lower bound. The edge list of the source paper's proposed graph is absent from the prompt, so I do not assert that it is \(F\), although \(m_{\rm pair}(F)=4/9\) puts \(F\) in exactly the numerical window highlighted in the question.

# 5. A specific recurrence for \(C_5^{(3)-}\)

Let \(G\) be an \(F\)-free 3-graph, where \(F\) is given by (4.1). For \(v\in V(G)\), let \(L_v\) be its link graph:
\[
xy\in E(L_v)\quad\Longleftrightarrow\quad vxy\in E(G).
\]

## Lemma 5.1: link paths force blue triples

If \(a-b-c-d\) is a four-vertex path in \(L_v\), then neither \(abd\) nor \(acd\) is an edge of \(G\).

### Proof

If \(abd\in E(G)\), then under
\[
(1,2,3,4,5)=(v,b,c,a,d)
\]
the four edges of \(F\) become
\[
vbc,\quad vba,\quad vcd,\quad bad,
\]
all red.

If \(acd\in E(G)\), use
\[
(1,2,3,4,5)=(v,c,b,d,a).
\]
The four required edges become
\[
vcb,\quad vcd,\quad vba,\quad cda.
\]
Again this is a red \(F\). ∎

## Corollary 5.2: complete bipartite links give blue joins

Suppose \(L_v\) contains a complete bipartite graph with parts \(A,B\), where \(|A|,|B|\ge2\). Then every triple meeting both \(A\) and \(B\) is absent from \(G\).

### Proof

For \(a_1,a_2\in A\), \(b\in B\), choose \(b'\in B\setminus\{b\}\). Then
\[
a_1-b'-a_2-b
\]
is a path in \(L_v\), so Lemma 5.1 makes \(a_1a_2b\) blue. The case of one vertex in \(A\) and two in \(B\) is symmetric. ∎

Let \(R(n)=R_F(n)\).

## Proposition 5.3

There is an absolute constant \(C\) such that, for all \(n\ge5\),
\[
R(n)\le Cn^4R(n-2). \tag{5.1}
\]

### Proof

Put \(t=R(n-2)\), and suppose \(G\) is an \(F\)-free 3-graph on \(N\) vertices with \(\alpha(G)<n\).

No link \(L_v\) contains \(K_{2,t}\). Indeed, if \(A,B\) are the two parts with \(|A|=2\), \(|B|=t\), then \(G[B]\), being \(F\)-free, contains an independent set \(Q\) of size \(n-2\). Corollary 5.2 says all triples meeting both \(A\) and \(B\) are blue. Therefore \(A\cup Q\) is an independent \(n\)-set, a contradiction.

A \(K_{2,t}\)-free graph \(L\) on \(m\) vertices satisfies
\[
e(L)\le m+\sqrt t\,m^{3/2}. \tag{5.2}
\]
Indeed, every pair has at most \(t-1\) common neighbors, so
\[
\sum_x\binom{d(x)}2\le(t-1)\binom m2.
\]
Using Cauchy–Schwarz on \(\sum_xd(x)^2\) gives (5.2).

Summing over all links and using
\[
\sum_v e(L_v)=3e(G)
\]
gives
\[
e(G)\le C_1\bigl(N^2+\sqrt t\,N^{5/2}\bigr).
\]
For \(N\ge t\), this is at most
\[
C_2\sqrt t\,N^{5/2}.
\]

The elementary alteration bound used earlier yields
\[
\alpha(G)\ge c\frac{N^{3/2}}{\sqrt{e(G)}}
          \ge c'\left(\frac Nt\right)^{1/4}.
\]
Thus \(N\ge Cn^4t\), with \(C\) sufficiently large, forces \(\alpha(G)\ge n\), contradiction. This proves (5.1). ∎

Iterating (5.1) gives
\[
R(n)\le 2^{O(n\log n)}.
\]
More explicitly, for even \(n=2m\),
\[
R(2m)
 \le R(2)\,C^{m-1}\prod_{j=2}^m(2j)^4
 =2^{2n\log_2 n+O(n)}.
\]

# 6. Why this does not yield \(2^{O(n)}\)

The loss is explicit. The \(K_{2,t}\)-free link estimate and alteration argument only give
\[
\alpha(G)\ge c(N/t)^{1/4}.
\]
To gain two vertices in the independent set, one must therefore enlarge the host by a factor of order \(n^4\). Iterating this over \(\Theta(n)\) stages produces the \(\log n\) in the exponent.

Removing this factor is not a matter of optimizing constants in the Kővári–Sós–Turán calculation. One would need a genuinely global statement exploiting the simultaneous structure of all links of an \(F\)-free 3-graph. The present argument treats the links separately and then applies a completely general independence bound; that is precisely where potentially decisive information is discarded.

For reference, \(F\) has a strong homomorphism to \(K_4^{(3)-}\): map
\[
1\mapsto A,\quad 2\mapsto B,\quad 3,4\mapsto C,\quad 5\mapsto D,
\]
where the target edges are
\[
ABC,\quad ACD,\quad BCD.
\]
Thus \(F\subseteq K_4^{(3)-}(2)\), and Proposition 2.1 also recovers a \(2^{O(n\log n)}\) upper bound from that for \(K_4^{(3)-}\). This quotient cannot give a purely exponential upper bound because \(K_4^{(3)-}\) itself has the quoted \(2^{\Omega(n\log n)}\) lower bound.

# 7. Final status and exact gap

The conjecture is not resolved here.

The rigorous progress is:

- fixed blow-ups and strong homomorphic images change \(\log R_H(n)\) by only a constant factor;
- pair-neighborhood suspension satisfies
  \[
  R_{\Sigma_2(F)}(n)\le C_Fn^2R_F(n);
  \]
- among 3-graphs on at most five vertices, only \(C_5^{(3)-}\) can possibly have a purely exponential rate;
- for \(C_5^{(3)-}\),
  \[
  R(n)\le Cn^4R(n-2)=2^{O(n\log n)}.
  \]

What remains is either:

1. prove \(R_{C_5^{(3)-}}(n)\le2^{O(n)}\), if this graph has the reported exponential lower bound; or
2. apply the strong-quotient test to the actual larger candidate from the source paper and find a quotient with a known \(2^{O(n)}\) upper bound.

Neither step is completed.