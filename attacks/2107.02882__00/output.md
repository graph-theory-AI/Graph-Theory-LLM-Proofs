```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The standard neighborhood-split transfer yields both kernel lower bounds at twin-width 6, and an explicit twin-width-4 graph shows that this transfer can require width exactly 6, so it cannot settle the requested bound 4.",
  "would_publish": false,
  "caveats": "The exact twin-width-4 lower bounds remain open, and the width-6 consequence may overlap the source paper's bounded-width constructions."
}
```

# 1. Statement of the partial result

For a graph \(G\), let \(\gamma(G)\), \(\gamma_c(G)\), and \(\gamma_t(G)\) denote its domination, connected-domination, and total-domination numbers.

I prove the following generic transfer.

### Proposition 1
Given a graph \(G\), construct the split graph \(S(G)\) with vertex set
\[
\{s_v:v\in V(G)\}\,\dot\cup\,\{t_v:v\in V(G)\}
\]
such that

* the vertices \(s_v\) form a clique;
* the vertices \(t_v\) form an independent set;
* \(s_vt_u\in E(S(G))\) exactly when \(u=v\) or \(uv\in E(G)\).

Then
\[
\gamma_c(S(G))=\gamma(G)
\]
and, for every nonempty \(G\),
\[
\gamma_t(S(G))=\max\{2,\gamma(G)\}.
\]
Moreover, from a supplied \(d\)-sequence of \(G\), one can construct in polynomial time a supplied \((d+2)\)-sequence of \(S(G)\).

Consequently, the source paper's lower bound for \(k\)-Dominating Set at twin-width \(4\) implies the corresponding no-polynomial-kernel results for Connected \(k\)-Dominating Set and Total \(k\)-Dominating Set at twin-width at most \(6\), with the sequence supplied.

The additive loss of two is not merely an artifact of the proof:

### Proposition 2
There is a graph \(Q\) with \(\operatorname{tww}(Q)\le 4\) such that
\[
\operatorname{tww}(S(Q))=6.
\]
One may take
\[
Q=C_4\square C_4=K_{2,2}\square K_{2,2}.
\]

Thus no better analysis of this standard split-neighborhood transformation can prove the requested twin-width-\(4\) result: the transformed graph can genuinely have twin-width \(6\).

# 2. Semantic equivalence

Let \(D\subseteq V(G)\) be a dominating set. Then
\[
S_D:=\{s_v:v\in D\}
\]
dominates \(S(G)\): the clique side is dominated by any member of \(S_D\), and \(t_u\) is dominated exactly when \(u\in N_G[D]\). Since \(S_D\) induces a clique, it is connected. Hence
\[
\gamma_c(S(G))\le \gamma(G).
\]

Conversely, let \(C\) be a connected dominating set of \(S(G)\), and put
\[
P=\{v:s_v\in C\text{ or }t_v\in C\}.
\]
For every \(u\):

* if \(t_u\notin C\), then \(t_u\) must be dominated by some \(s_v\in C\), so \(u\in N_G[v]\);
* if \(t_u\in C\), then \(u\in P\), and \(s_u\) would dominate \(t_u\).

Thus \(\{s_v:v\in P\}\) is a dominating set of \(S(G)\), and \(P\) is a dominating set of \(G\). Also,
\[
|P|\le |C|.
\]
It follows that
\[
\gamma(G)\le\gamma_c(S(G)).
\]
Therefore
\[
\gamma_c(S(G))=\gamma(G).
\]

For total domination, if \(D\) is a dominating set of \(G\) of size at least two, then \(S_D\) is a total dominating set of \(S(G)\): the selected clique vertices dominate each other, and they dominate all \(t_u\). If \(\gamma(G)=1\), one can use two clique vertices when \(|V(G)|\ge2\), or \(\{s_v,t_v\}\) when \(G\) has one vertex. Hence
\[
\gamma_t(S(G))\le\max\{2,\gamma(G)\}.
\]

Conversely, let \(C\) be a total dominating set of \(S(G)\). Since the \(t\)-side is independent, every \(t_u\), selected or not, has a selected neighbor on the \(s\)-side. Consequently
\[
\{v:s_v\in C\}
\]
already dominates \(G\). Thus
\[
\gamma(G)\le |C|.
\]
Every total dominating set has size at least two, proving
\[
\gamma_t(S(G))=\max\{2,\gamma(G)\}.
\]

For a parameterized reduction, the case \(k<2\) can be decided directly; for \(k\ge2\),
\[
\gamma(G)\le k
\quad\Longleftrightarrow\quad
\gamma_t(S(G))\le k.
\]

# 3. The \((d+2)\)-sequence

Use the partition formulation of twin-width: at a partition of the original vertex set, two parts are joined by a red edge exactly when the bipartite adjacency between them is neither complete nor empty.

Let \(\mathcal P\) be a partition occurring in a supplied \(d\)-sequence of \(G\). For \(X\in\mathcal P\), write
\[
S_X=\{s_v:v\in X\},\qquad T_X=\{t_v:v\in X\}.
\]
Consider the lifted partition
\[
\widehat{\mathcal P}=\{S_X,T_X:X\in\mathcal P\}.
\]

Pairs of \(S\)-parts are complete, and pairs of \(T\)-parts are empty. For distinct \(X,Y\), the block \(S_X\times T_Y\) is mixed exactly when the pair \(X,Y\) is red in the quotient of \(G\). The diagonal block \(S_X\times T_X\) may contribute one additional red neighbor. Therefore every part of \(\widehat{\mathcal P}\) has red degree at most \(d+1\).

Suppose the next contraction in \(G\) merges \(A,B\) into \(C=A\cup B\). Simulate it in \(S(G)\) by

1. merging \(S_A,S_B\) into \(S_C\);
2. merging \(T_A,T_B\) into \(T_C\).

At the intermediate partition:

* \(S_C\) has at most \(d\) mixed blocks \(T_Y\) for \(Y\notin\{A,B\}\), corresponding to red neighbors of \(C\) after the base contraction, plus the two exceptional blocks \(T_A,T_B\);
* any unchanged \(S_X\) has at most \(d\) off-diagonal mixed blocks and its possible diagonal block;
* any unchanged \(T_Y\) has at most \(d\) off-diagonal mixed blocks and its possible diagonal block;
* each of \(T_A,T_B\) has at most \(d\) old mixed neighbors plus the exceptional new block \(S_C\).

Thus the intermediate red degree is at most \(d+2\). After the second contraction the partition is again synchronized, with red degree at most \(d+1\).

Repeating this for all base contractions leaves \(S_{V(G)}\) and \(T_{V(G)}\), which can finally be contracted with width at most one. Hence
\[
\operatorname{tww}(S(G))\le \operatorname{tww}_{\text{given sequence}}(G)+2.
\]

# 4. Tightness: a twin-width-\(4\) graph whose split lift has twin-width \(6\)

Let
\[
Q=K_{2,2}\square K_{2,2}.
\]
Label its vertices by four bits
\[
(p,a,q,b)\in\{0,1\}^4.
\]
Adjacency is given by either

\[
(p,a,q,b)\sim(1-p,a',q,b)
\quad\text{for either }a',
\]
or
\[
(p,a,q,b)\sim(p,a,1-q,b')
\quad\text{for either }b'.
\]

## 4.1 A \(4\)-sequence for \(Q\)

First, for every fixed \((p,q,b)\), contract the two vertices differing only in \(a\). Denote the resulting bag by \(A_{pqb}\).

A newly formed \(A_{pqb}\):

* is completely adjacent to the corresponding horizontal pair with first coordinate \(1-p\);
* has mixed adjacency to at most four singleton bags in the opposite \(q\)-layer—two possible \(b'\), with two possible \(a\)'s.

Thus its red degree is at most four. An uncontracted singleton has red adjacency to at most two already contracted bags. After all these contractions, every \(A_{pqb}\) has red degree two.

Next, for every fixed \((p,q)\), contract \(A_{pq0}\) with \(A_{pq1}\), obtaining \(B_{pq}\). A newly formed \(B_{pq}\) has:

* at most two red neighbors in the opposite \(q\)-layer;
* at most two red neighbors in the opposite \(p\)-layer.

Hence this phase also has red degree at most four. At its end only four bags \(B_{pq}\) remain, and their red graph is a \(4\)-cycle. The remaining contractions clearly have width at most two. Therefore
\[
\operatorname{tww}(Q)\le4.
\]

## 4.2 Lower bound for \(S(Q)\)

The graph \(Q\) is \(4\)-regular and triangle-free. Furthermore, two nonadjacent vertices have at most two common neighbors. Consequently, for distinct \(u,v\),
\[
|N_Q[u]\triangle N_Q[v]|\ge6.
\]
Indeed:

* if \(u,v\) are adjacent, their closed neighborhoods have size five and intersect exactly in \(\{u,v\}\);
* if they are nonadjacent, their closed neighborhoods each have size five and intersect in at most two common neighbors.

Consider the first contraction in any sequence for \(S(Q)\).

* If it contracts \(s_u,s_v\), the new bag has a red neighbor \(t_w\) for every
  \[
  w\in N_Q[u]\triangle N_Q[v],
  \]
  giving red degree at least six.
* The same argument applies to \(t_u,t_v\).
* If it contracts \(s_u,t_v\), the red degree is actually \(15\). Among the remaining \(s\)-vertices and \(t\)-vertices, the two contracted vertices disagree on exactly
  \[
  \bigl(15-|N_Q[v]\setminus\{u\}|\bigr)
  +|N_Q[u]\setminus\{v\}|=15
  \]
  adjacencies.

Thus every possible first contraction creates red degree at least six, and
\[
\operatorname{tww}(S(Q))\ge6.
\]
Proposition 1 supplies a \(6\)-sequence, so
\[
\operatorname{tww}(S(Q))=6.
\]

# 5. A precise alternative route

For a \(0/1\) incidence matrix \(M\), form the split graph \(S(M)\) by making row vertices a clique, column vertices independent, and using \(M\) for the cross adjacencies. If every column contains a \(1\), then the connected-domination number of \(S(M)\) is exactly the minimum number of rows covering all columns. Its total-domination number is the maximum of that covering number and \(2\).

Moreover, if \(M\) is supplied with a sequence of row and column mergers in which every block has at most four opposite blocks on which the matrix is mixed, then the same mergers give a \(4\)-sequence of \(S(M)\).

Therefore a direct kernel lower bound for Set Cover on incidence matrices having such a mixed-degree-\(4\) sequence would establish both requested results. What Proposition 2 shows is that one cannot obtain the needed matrix sequence merely by taking the closed-neighborhood matrix of an arbitrary graph supplied with a \(4\)-sequence.

# 6. Remaining gap

The requested twin-width-\(4\) lower bounds are not proved here. A successful proof must redesign the hard instances so that connectivity and total support are built into the width-\(4\) contraction sequence, rather than applying the standard closed-neighborhood split lift. The explicit graph \(C_4\square C_4\) shows that this is a genuine structural obstruction: the natural reduction has an unavoidable jump from \(4\) to \(6\), even under an optimal contraction sequence.