```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An exact criterion is proved for a fixed cubic 2-factor with two odd circuits, yielding the conjecture for cyclically 4-edge-connected cubic graphs of oddness at most two, as well as for all supereulerian and nowhere-zero-4-flow graphs.",
  "would_publish": false,
  "caveats": "The argument does not handle general cubic graphs with four or more odd factor circuits, or all graphs with obstructing cyclic 3-edge-cuts; novelty relative to the very recent companion literature has not been checked."
}
```

# 1. Statement and conventions

An integer \(k\)-flow is a circulation taking values in
\[
\{-(k-1),\ldots,-1,0,1,\ldots,k-1\}.
\]
Orientations used below may differ between constructions; equivalently, all values can be transferred to one fixed orientation by changing signs.

A pair \((\varphi _2,\varphi _4)\) is a \(1/2\)-flow-pair if
\[
\varphi _2(e)=0\quad\Longrightarrow\quad |\varphi _4(e)|\ge 2.
\]

The full conjecture is not proved. I establish several rigorous special cases, the main one being an exact result for cubic graphs whose chosen 2-factor has exactly two odd circuits.

Loops are harmless: one may delete them and later assign \(\varphi _2=1,\varphi _4=0\) to each loop. Thus cubic statements below are for loopless multigraphs.

# 2. Reduction to cubic graphs

## Proposition 2.1
If every bridgeless cubic multigraph admits a \(1/2\)-flow-pair, then every bridgeless graph does.

### Proof
It is enough to consider a connected loopless bridgeless graph \(G\); then every vertex has degree at least two.

Replace every vertex \(v\) of degree \(d(v)\) by a cycle \(C_v\) of length \(d(v)\), and attach the \(d(v)\) incident edge-ends one per vertex of \(C_v\). A 2-cycle is allowed when \(d(v)=2\). The resulting graph \(\widehat G\) is cubic.

It is also bridgeless:

- an edge of a replacement cycle has the other arc of that cycle as an alternative route;
- an old edge lies on a cycle of \(G\), and that cycle lifts through the replacement cycles to an alternative route in \(\widehat G\).

Suppose \(\widehat G\) has a \(1/2\)-flow-pair. Restrict both flows to the old edges and contract each \(C_v\). Summing the conservation equations over all vertices of \(C_v\) cancels the internal edges, so the restrictions are flows on \(G\). The compatibility condition on every old edge is inherited. ∎

Thus the cubic case is genuinely central.

# 3. What a pair looks like in a cubic graph

## Proposition 3.1
Let \(G\) be a loopless cubic graph with a \(1/2\)-flow-pair. Then the support of \(\varphi _2\) is a spanning 2-factor \(F\), and \(M=E(G)\setminus F\) is a perfect matching. Conversely, it suffices to find a 2-factor \(F\) and a 4-flow satisfying
\[
|\varphi _4(e)|\ge 2\qquad(e\in E(G)\setminus F).
\]

### Proof
At a cubic vertex, the number of incident nonzero values of a 2-flow is even: three numbers from \(\{\pm1\}\) cannot sum to zero. Hence the support degree is either zero or two.

Support degree zero is impossible. Indeed, compatibility would force all three incident 4-flow values to have magnitudes in \(\{2,3\}\). Three signed numbers of magnitudes two or three cannot sum to zero: one of them would have to equal in magnitude the sum of the other two, but the former is at most three and the latter at least four.

Therefore the support degree is two at every vertex. It is consequently a spanning union of circuits, and its complement is a perfect matching. The converse follows by orienting every circuit of \(F\) cyclically and assigning value one to its edges. ∎

So the cubic conjecture can be stated as follows:

> Every bridgeless cubic graph has a 2-factor \(F\) and a 4-flow whose values on the complementary perfect matching have magnitudes two or three.

# 4. A general even-component construction

The following gives, in particular, all Hamiltonian and more generally all supereulerian graphs.

## Lemma 4.1 — even-component criterion
Let \(H\) be a spanning even subgraph of \(G\). Isolated vertices are allowed as components of \(H\). Suppose that, for every component \(K\) of \(H\), the number of edge-ends of \(E(G)\setminus E(H)\) incident with vertices of \(K\), with loops counted twice, is even. Then \(G\) admits a \(1/2\)-flow-pair with
\[
\operatorname{supp}(\varphi _2)=E(H).
\]

### Proof
Orient an Euler tour in every nontrivial component of \(H\), and set \(\varphi _2=1\) along those tours and zero outside \(H\).

Write \(Z=E(G)\setminus E(H)\). For every incidence of an edge of \(Z\) with a component of \(H\), make one token. For each component \(K\), place its tokens in a linear order along a chosen Euler tour, allocating a token at an occurrence of its incident vertex. Pair consecutive tokens:
\[
(1,2),(3,4),\ldots.
\]
This is possible by the parity hypothesis. At an isolated vertex, simply choose any ordering of its tokens.

Construct an auxiliary graph whose vertices are the tokens and whose edges are of two types:

1. pair the two endpoint-tokens belonging to each edge of \(Z\);
2. join each consecutive pair chosen inside a component of \(H\).

Every token has degree two, and every auxiliary circuit alternates between the two types of pairing. Hence every auxiliary circuit is even. We may therefore assign signs \(\varepsilon\in\{+1,-1\}\) to the tokens so that paired tokens always receive opposite signs.

Orient every edge \(e\in Z\) from its \(+\)-token to its \(-\)-token and give it 4-flow value \(2\). In each component \(K\), consecutive token-pairs have opposite signs. Consequently every prefix sum of token signs is in \(\{-1,0,1\}\), and the total sum is zero.

Split an Euler tour temporarily at its successive vertex-occurrences. If \(b_i\) is twice the sum of signs of tokens allocated at the \(i\)-th occurrence, assign values to successive tour edges recursively so that
\[
x_i-x_{i-1}+b_i=0.
\]
The total sum of the \(b_i\)'s is zero, so the recursion closes around the tour. Moreover every \(x_i\) is minus twice a token-prefix sum, and hence
\[
|x_i|\le 2.
\]
After identifying repeated occurrences of the same vertex, conservation still holds. At an isolated component, the signed external values already sum to zero.

This defines a 4-flow. Every edge outside \(H\), precisely where \(\varphi _2\) vanishes, has 4-flow magnitude two. ∎

## Corollary 4.2
Every graph containing a connected spanning Eulerian subgraph admits a \(1/2\)-flow-pair.

Indeed, there is only one component of \(H\), and the number of external edge-ends is \(2|E(G)\setminus E(H)|\).

Thus the conjecture holds for all supereulerian graphs, in particular for all Hamiltonian graphs.

# 5. Two even subgraphs covering all edges

There is another standard sufficient condition.

## Proposition 5.1
Suppose \(A\) and \(B\) are even subgraphs of \(G\) with
\[
E(G)=E(A)\cup E(B).
\]
Then \(G\) has a \(1/2\)-flow-pair.

### Proof
Orient each component of \(A\) and \(B\) Eulerianly, obtaining 2-flows \(\alpha,\beta\) supported on \(A,B\), respectively. Set
\[
\varphi _2=\alpha,\qquad \varphi _4=\alpha+2\beta.
\]
The latter is a 4-flow because its values have magnitude at most three. If \(\alpha(e)=0\), then coverage implies \(\beta(e)\ne0\), and hence
\[
|\varphi _4(e)|=2.
\]
∎

The coordinate supports of a nowhere-zero \(\mathbb Z_2^2\)-flow provide such \(A,B\). Hence this proves the conjecture for every graph admitting a nowhere-zero 4-flow in the standard Tutte sense. Consequences include:

- every 3-edge-colourable cubic graph;
- every bridgeless planar graph, by planar duality and the Four Colour Theorem.

# 6. Main partial result: a fixed 2-factor with two odd circuits

Let \(G\) be a connected loopless cubic graph, let \(F\) be a 2-factor, and let
\[
M=E(G)\setminus E(F).
\]
Contract every circuit of \(F\) to one vertex, retaining loops and parallel edges, and denote the resulting multigraph by
\[
Q=G/F.
\]
The degree of a vertex of \(Q\), counting loops twice, equals the length of its corresponding factor circuit. Thus the odd-degree vertices of \(Q\) are exactly the odd circuits of \(F\).

## Theorem 6.1 — exact two-odd-circuit criterion
Suppose \(F\) has exactly two odd circuits, corresponding to vertices \(A,B\) of \(Q\). There is a \(1/2\)-flow-pair with
\[
\operatorname{supp}(\varphi _2)=E(F)
\]
if and only if every \(A\)-\(B\) edge-cut of \(Q\) has size at least five.

### Necessity

Suppose such a pair exists. Every matching edge has 4-flow magnitude two or three. Contracting the factor circuits turns the values on \(M\) into a flow on \(Q\): conservation at a contracted vertex follows by summing conservation over the corresponding factor circuit.

Every \(A\)-\(B\) cut of \(Q\) has odd cardinality. Indeed, if \(A\in X\) and \(B\notin X\), then
\[
|\delta_Q(X)|\equiv \sum_{v\in X}d_Q(v)\equiv1\pmod 2.
\]
If an \(A\)-\(B\) cut had size less than five, it would therefore have size one or three.

A one-edge cut plainly cannot carry a flow with a nonzero value. Across a three-edge cut, conservation would require three signed numbers from \(\{\pm2,\pm3\}\) to sum to zero. This is impossible: if one sign differs from the other two, its magnitude is at most three while the sum of the other two magnitudes is at least four. Thus every \(A\)-\(B\) cut has size at least five.

### Sufficiency

Assume every \(A\)-\(B\) cut has size at least five.

#### Step 1: A locally balanced orientation of \(Q\)

At each vertex \(v\) of \(Q\), list its incidences in the cyclic order inherited from the corresponding factor circuit. A loop contributes two incidences.

- At every even-degree vertex, pair incidences \(1\) with \(2\), \(3\) with \(4\), and so forth.
- At \(A\) and \(B\), pair all incidences except the last one.

Make an auxiliary graph whose vertices are the incidences of \(Q\). Join:

1. the two incidences belonging to each edge of \(Q\);
2. every locally paired pair of incidences.

Every auxiliary component is an even alternating circuit, except for one alternating path joining the unpaired incidence at \(A\) to the unpaired incidence at \(B\). Assign signs \(\varepsilon\in\{\pm1\}\) to incidences so that adjacent incidences in the auxiliary graph have opposite signs. Choose the sign on the path so that the unpaired incidence at \(A\) has sign \(+1\), and hence the one at \(B\) has sign \(-1\).

The two incidences of every edge have opposite signs, so orient each edge from its \(+\)-incidence to its \(-\)-incidence. Let
\[
r(v)=d^+(v)-d^-(v).
\]
The local pairs cancel, giving
\[
r(A)=1,\qquad r(B)=-1,\qquad r(v)=0\quad(v\ne A,B).
\]

Moreover, if
\[
D_{v,j}=\sum_{i=1}^j\varepsilon_{v,i}
\]
is a prefix sum in the inherited incidence order, then
\[
D_{v,j}\in\{-1,0,1\}.
\tag{6.1}
\]

#### Step 2: Two directed paths against the imbalance

Let \(X\subseteq V(Q)\) contain \(B\) but not \(A\). Summing the unit divergences over \(X\) gives
\[
d^+(X)-d^-(X)=-1.
\]
Writing \(k=|\delta_Q(X)|\), it follows that
\[
d^+(X)=\frac{k-1}{2}.
\]
By hypothesis \(k\ge5\), and therefore \(d^+(X)\ge2\).

Thus every directed cut separating \(B\) from \(A\) contains at least two arcs directed out of the \(B\)-side. By the integral max-flow/min-cut theorem, there are two edge-disjoint directed paths
\[
P_1,P_2:B\longrightarrow A.
\]
They may be chosen vertex-simple individually.

Give every edge of \(P_1\cup P_2\) weight three and every other edge of \(Q\) weight two. At \(A\), the two paths contribute two additional incoming units; at \(B\), they contribute two additional outgoing units; and at every other vertex their additional contributions balance. Consequently the weighted orientation is a flow:
\[
\sum_{\text{out of }v}w(e)-\sum_{\text{into }v}w(e)=0.
\tag{6.2}
\]

#### Step 3: Controlling the order around each factor circuit

For the first \(j\) incidences at \(v\), let
\[
U_{v,j}=\sum_{\substack{i\le j\\ e_i\in P_1\cup P_2}}\varepsilon_{v,i}.
\]
Because each path is vertex-simple, at an internal vertex each path contributes at most one entering and one leaving incidence. Hence, over all prefixes,
\[
\max_j U_{v,j}-\min_j U_{v,j}\le2.
\tag{6.3}
\]
The same bound holds at \(A\) and \(B\), where there are simply two incoming or two outgoing path-incidences.

The prefix sum of the weighted matching-edge divergences is
\[
S_{v,j}=2D_{v,j}+U_{v,j}.
\]
By (6.1) and (6.3),
\[
\max_j S_{v,j}-\min_j S_{v,j}\le 4+2=6.
\tag{6.4}
\]
Equation (6.2) says that the full sum \(S_{v,d(v)}\) is zero.

#### Step 4: Lifting the flow from \(Q\) to \(G\)

Orient every circuit \(C_v\) of \(F\) according to its incidence order. Let \(a_i\) be the signed matching-edge value at its \(i\)-th vertex, and put
\[
S_i=a_1+\cdots+a_i.
\]
Since the matching values form a flow on \(Q\), \(S_{|C_v|}=0\).

Assign to the factor edge leaving the \(i\)-th vertex the value
\[
x_i=c_v-S_i.
\]
Then at the \(i\)-th vertex,
\[
x_i-x_{i-1}+a_i=0,
\]
so conservation holds. By (6.4), the range of the \(S_i\)'s has width at most six. Therefore there is an integer \(c_v\) satisfying
\[
\max_i S_i-3\le c_v\le \min_i S_i+3,
\]
and hence
\[
|x_i|\le3
\]
for every factor edge.

This constructs a 4-flow on \(G\), with every edge of \(M\) having magnitude two or three. Finally orient every factor circuit cyclically and set
\[
\varphi _2(e)=
\begin{cases}
1,&e\in F,\\
0,&e\in M.
\end{cases}
\]
The resulting pair has the required compatibility. ∎

# 7. Consequences

## Corollary 7.1
Every cyclically 4-edge-connected cubic graph of oddness at most two admits a \(1/2\)-flow-pair.

### Proof
If the oddness is zero, choose an all-even 2-factor. Lemma 4.1 applies because every factor circuit has an even number of complementary matching incidences.

Suppose the oddness is two, and choose a 2-factor with exactly two odd circuits \(A,B\). If the quotient \(Q\) had an \(A\)-\(B\) cut of size less than five, parity would make its size one or three. Its preimage in \(G\) consists solely of matching edges and separates two subgraphs each containing a factor circuit. It would therefore be a cyclic edge-cut of size less than four, contrary to cyclic 4-edge-connectivity. Apply Theorem 6.1. ∎

## Corollary 7.2
Every cubic graph consisting of two disjoint circuits joined by a perfect matching admits a \(1/2\)-flow-pair.

For even circuit length this follows from Lemma 4.1. For odd length at least five, the quotient consists of two vertices joined by at least five parallel edges, so Theorem 6.1 applies. The length-three case is the triangular prism, which is Hamiltonian.

# 8. Explicit Petersen-graph instance

This also gives a direct check on the construction.

Write the Petersen graph as outer circuit
\[
c_0c_1c_2c_3c_4c_0
\]
and inner circuit, in cyclic order,
\[
u_0u_2u_4u_1u_3u_0,
\]
with spokes \(c_i u_i\).

Orient spokes \(0,3,4\) from \(c_i\) to \(u_i\), with value \(2\), and spokes \(1,2\) from \(u_i\) to \(c_i\), with value \(3\). Around the outer circuit, oriented \(c_i\to c_{i+1}\), assign successive values
\[
-3,\ 0,\ 3,\ 1,\ -1.
\]
Around the inner circuit in the displayed order, assign
\[
2,\ -1,\ 1,\ -2,\ 0.
\]
A direct vertex-by-vertex calculation gives conservation. The two 5-circuits, each carrying unit 2-flow, form the support of \(\varphi _2\), and every spoke has 4-flow magnitude two or three.

# 9. Remaining gap

After Proposition 3.1, the unresolved cubic problem is to choose a suitable 2-factor. Theorem 6.1 completely handles a fixed factor with exactly two odd circuits: a separating one- or three-edge cut in the quotient is the only obstruction for that factor.

With four or more odd factor circuits, the incidence-pairing construction leaves four or more unmatched terminals. Correcting the resulting unit imbalances requires routing two additional units between several terminals while retaining both edge capacity one for the “upgrade from \(2\) to \(3\)” and the width-six prefix bound around every factor circuit. The natural cut inequalities in this multiflow problem are already of the same \(5\)-to-\(1\) form that appears in 5-flow theory. I do not have an argument satisfying these inequalities in general.

Thus the conjecture remains open, but the cyclically 4-edge-connected oddness-\(\le2\) case and the exact two-odd-circuit criterion are fully proved above.