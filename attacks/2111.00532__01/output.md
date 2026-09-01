```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "Under the standard fixed-position meaning of an ordered transversal copy, every finite ordered graph H has the requested property, with exponent c=1/(|H|-1).",
  "would_publish": false,
  "caveats": "The catalog statement is probably missing a stronger requirement, since the literal formulation has the elementary proof below."
}
```

## Statement proved

Let \(H\) be an ordered graph with ordered vertex set
\[
h_1<h_2<\cdots<h_k,\qquad k\ge 2.
\]
Let \(G\) contain a blockade
\[
\mathcal B=(B_1,\ldots,B_k)
\]
of width \(W\), so \(|B_i|\ge W\) for every \(i\). An ordered \(\mathcal B\)-transversal copy of \(H\) means a choice \(v_i\in B_i\) such that
\[
v_iv_j\in E(G)\quad\Longleftrightarrow\quad h_ih_j\in E(H)
\]
for all \(i<j\).

Then, if no such copy exists, there are distinct \(i,j\) and a pure pair
\[
X\subseteq B_i,\qquad Y\subseteq B_j
\]
such that
\[
|X|,|Y|
 \ge
 \frac{1}{2(k-1)^{1/(k-1)}}W^{1/(k-1)}.
\]
Thus the question as extracted has the answer “all finite ordered graphs,” with
\[
c(H)=\frac1{|H|-1}.
\]

The same conclusion holds if the blockade has more than \(k\) blocks and the hypothesis excludes an ordered copy on every increasing choice of \(k\) blocks.

## Multipartite clique lemma

We use the following elementary labeled multipartite form of the Erdős–Hajnal–Pach embedding argument.

### Lemma

Let \(k\ge2\) and \(t\ge1\) be integers. Let \(F\) be a graph with pairwise disjoint vertex sets
\[
V_1,\ldots,V_k
\]
such that
\[
|V_i|\ge (k-1)t^{k-1}
\]
for every \(i\). Then at least one of the following holds:

1. \(F\) has a transversal clique, that is, vertices \(v_i\in V_i\) which are pairwise adjacent;
2. for some \(i<j\), there are \(X\subseteq V_i\) and \(Y\subseteq V_j\), each of size \(t\), with no edges of \(F\) between \(X\) and \(Y\).

### Proof

We induct on \(k\).

For \(k=2\), if there is no transversal \(K_2\), then there are no edges between \(V_1\) and \(V_2\), and any \(t\)-subsets give the second outcome.

Now let \(k\ge3\), and suppose neither conclusion holds. Fix \(v\in V_k\). We claim that for some \(i<k\),
\[
|N_F(v)\cap V_i|<(k-2)t^{k-2}. \tag{1}
\]
Indeed, otherwise choose
\[
U_i\subseteq N_F(v)\cap V_i,\qquad |U_i|=(k-2)t^{k-2}
\]
for every \(i<k\). Applying the induction hypothesis to \(U_1,\ldots,U_{k-1}\), either:

- there is a transversal \(K_{k-1}\), which together with \(v\) forms a transversal \(K_k\); or
- two of the \(U_i\)'s contain anticomplete \(t\)-subsets.

Both contradict our assumption. Hence (1) holds for every \(v\in V_k\).

Assign to each \(v\in V_k\) one index \(i(v)<k\) satisfying (1). By the pigeonhole principle, for some \(i<k\), the set
\[
Y_0=\{v\in V_k:i(v)=i\}
\]
has size at least
\[
\frac{|V_k|}{k-1}\ge t^{k-1}\ge t.
\]
Choose \(Y\subseteq Y_0\) with \(|Y|=t\). Its total neighborhood in \(V_i\) has size less than
\[
t(k-2)t^{k-2}=(k-2)t^{k-1}.
\]
Since
\[
|V_i|\ge(k-1)t^{k-1},
\]
there are at least \(t^{k-1}\ge t\) vertices of \(V_i\) with no neighbor in \(Y\). Choosing \(t\) of them gives an anticomplete pair, contrary to assumption. This proves the lemma. \(\square\)

## Reduction of an arbitrary ordered graph to a clique

For each pair \(i<j\), define a new cross-block adjacency relation \(F\) by declaring \(xy\), with \(x\in B_i\) and \(y\in B_j\), to be an edge of \(F\) exactly when the adjacency of \(x,y\) in \(G\) agrees with the prescribed adjacency of \(h_i,h_j\) in \(H\):
\[
xy\in E(F)
\quad\Longleftrightarrow\quad
\bigl(xy\in E(G)\bigr)
\Longleftrightarrow
\bigl(h_ih_j\in E(H)\bigr).
\]
Equivalently:

- if \(h_ih_j\in E(H)\), retain the \(G\)-adjacency between \(B_i,B_j\);
- if \(h_ih_j\notin E(H)\), complement the \(G\)-adjacency between \(B_i,B_j\).

Edges inside individual blocks are irrelevant and may be defined arbitrarily.

A choice \(v_i\in B_i\) is a transversal clique in \(F\) precisely when
\[
G[\{v_1,\ldots,v_k\}]
\]
is an ordered \(\mathcal B\)-transversal copy of \(H\). Therefore the hypothesis says that \(F\) has no transversal \(K_k\).

Choose
\[
t=
\left\lfloor
\left(\frac{W}{k-1}\right)^{1/(k-1)}
\right\rfloor
\]
when \(W\ge k-1\). Then
\[
(k-1)t^{k-1}\le W,
\]
so the lemma supplies distinct \(i,j\) and \(t\)-sets
\[
X\subseteq B_i,\qquad Y\subseteq B_j
\]
which are anticomplete in \(F\).

Because all pairs between \(B_i\) and \(B_j\) have the same prescribed \(H\)-status, being anticomplete in \(F\) has one of two meanings:

- if \(h_ih_j\in E(H)\), then \(X,Y\) are anticomplete in \(G\);
- if \(h_ih_j\notin E(H)\), then \(X,Y\) are complete in \(G\).

Thus \((X,Y)\) is a pure pair in \(G\).

For \(W\ge k-1\), writing \(z=(W/(k-1))^{1/(k-1)}\ge1\), we have
\[
\lfloor z\rfloor\ge z/2,
\]
and hence
\[
t\ge
\frac{1}{2(k-1)^{1/(k-1)}}W^{1/(k-1)}.
\]
If \(W<k-1\), any two singleton subsets from different blocks form a pure pair, and the same displayed lower bound is less than \(1\). This proves the asserted uniform estimate.

For \(k=1\), a nonempty sole block always contains a transversal copy of the unique one-vertex graph, so the implication is vacuous.

## Conclusion and discrepancy with the catalog description

The literal formulation is not open: every ordered graph \(H\) satisfies it, and the proof depends only on \(|H|\). Indeed, independently complementing each pair of blocks according to the corresponding adjacency in \(H\) turns the forbidden ordered pattern into a forbidden transversal clique while preserving pure pairs.

Consequently, any intended question that distinguishes trees, caterpillars, and general ordered graphs must include an additional condition absent from the extracted statement—such as a prescribed stronger exponent, a near-linear bound, a one-sided conclusion, or a more robust blockade requirement. The argument above does not address such an omitted strengthening, nor does it determine the optimal exponent for a given \(H\).