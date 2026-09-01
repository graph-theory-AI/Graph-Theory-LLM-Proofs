```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every boundary class has an exact 2^(epsilon n) n^O(1) algorithm for each fixed epsilon>0, and S_{1,1,k}-free graphs admit an explicit 2^{O_k(n^{1-1/k} log n)} algorithm, but the polynomial-versus-NP-hard dichotomy remains open.",
  "would_publish": false,
  "caveats": "The qualitative all-H bound uses the bounded-degree algorithm quoted in the prompt; no polynomial algorithm or NP-hardness proof is obtained."
}
```

# 1. Statement and scope

All exclusions below are induced. Write \(\alpha(G)\) for the maximum size of an independent set of \(G\), and \(n=|V(G)|\).

I do not resolve the requested polynomial-time/NP-hardness dichotomy. I prove two upper bounds:

1. A general branching lemma lifts polynomial-time solvability at every fixed maximum degree to an arbitrarily small exponential base. Applied to the bounded-degree theorem quoted in the question, it covers every genuine subdivided claw \(S_{i,j,k}\).
2. For the infinite family \(S_{1,1,k}\), a direct structural lemma gives the explicit running time
   \[
   2^{O_k(n^{1-1/k}\log n)}.
   \]
   In particular, Maximum Independent Set on \(S_{1,1,3}\)-free graphs is solvable in
   \[
   2^{O(n^{2/3}\log n)}
   \]
   time.

These are exact algorithms, not approximation algorithms.

# 2. Lifting bounded-degree algorithms

## Theorem 2.1

Let \(\mathcal C\) be a hereditary graph class. Suppose that, for every fixed integer \(D\), Maximum Independent Set is solvable in polynomial time on graphs \(G\in\mathcal C\) with \(\Delta(G)\le D\).

Then for every fixed \(\varepsilon>0\), there is an exact algorithm for Maximum Independent Set on \(\mathcal C\) with running time
\[
2^{\varepsilon n}n^{O_{\mathcal C,\varepsilon}(1)}.
\]

If the bounded-degree algorithms and their running-time bounds are effective uniformly in \(D\), these algorithms can be diagonalized into a single \(2^{o(n)}\)-time algorithm.

## Proof

Fix \(D\). On a graph \(G\in\mathcal C\), use the following branching algorithm.

- If \(\Delta(G)\le D\), invoke the assumed polynomial-time bounded-degree algorithm.
- Otherwise choose, by a fixed deterministic rule, a vertex \(v\) with
  \(\deg(v)\ge D+1\), and use
  \[
  \alpha(G)=\max\bigl\{\alpha(G-v),\,1+\alpha(G-N[v])\bigr\}.
  \]

The class remains \(\mathcal C\) in both branches because \(\mathcal C\) is hereditary.

Consider a root-to-leaf path in the branching tree. Call a branch of the form \(G-N[v]\) an inclusion branch and one of the form \(G-v\) an exclusion branch. Every inclusion branch removes at least \(D+2\) currently present vertices. Consequently, a root-to-leaf path contains at most
\[
\left\lfloor\frac{n}{D+2}\right\rfloor
\]
inclusion branches and at most \(n\) branches in total.

Encoding a root-to-leaf path by its binary branch word, and including a factor \(n+1\) for the possible lengths, the number \(L_D(n)\) of leaves is at most
\[
L_D(n)
 \le (n+1)\sum_{r=0}^{\lfloor n/(D+2)\rfloor}\binom nr.
\]
Using the binary entropy function \(\mathrm H\),
\[
\sum_{r=0}^{\lfloor n/(D+2)\rfloor}\binom nr
 \le 2^{\,n\mathrm H(1/(D+2))}.
\]
Moreover,
\[
\mathrm H\!\left(\frac1{D+2}\right)
 \le \frac{\log_2(e(D+2))}{D+2}
 =O\!\left(\frac{\log D}{D}\right).
\]
Thus
\[
L_D(n)
 \le 2^{O(n\log D/D)}n^{O(1)}.
\]

For fixed \(D\), let the bounded-degree algorithm run in time \(c_Dn^{p_D}\). The total running time is therefore
\[
2^{O(n\log D/D)}n^{p_D+O(1)}.
\]
Given \(\varepsilon>0\), choose the fixed constant \(D\) sufficiently large that the coefficient of \(n\) in the exponential term is at most \(\varepsilon\). This proves
\[
T(n)\le 2^{\varepsilon n}n^{O_{\mathcal C,\varepsilon}(1)}.
\]
The same branching records an actual maximum independent set. \(\square\)

## Corollary 2.2: application to the catalog problem

Fix \(H=S_{i,j,k}\).

- If \(i\ge1\), then \(H\) is a genuine subdivided claw. The bounded-degree theorem quoted in the prompt supplies precisely the hypothesis of Theorem 2.1 for the hereditary class of \(H\)-free graphs.
- If \(i=0\), then \(H\) is a path, namely \(P_{j+k+1}\). The quoted quasi-polynomial algorithms are stronger. Even without them, the bounded-degree hypothesis is elementary: a connected \(P_t\)-free graph has diameter at most \(t-2\), so for fixed maximum degree it has bounded order.

Hence, for every \(H\) occurring in the stated boundary region and every fixed \(\varepsilon>0\),
\[
\operatorname{MIS}(H\text{-free})
   \quad\text{is solvable in}\quad
2^{\varepsilon n}n^{O_{H,\varepsilon}(1)}
\]
time.

This extends the quoted bounded-degree result to arbitrary degrees, albeit only with a subexponential-type exact upper bound.

# 3. An explicit bound for \(S_{1,1,k}\)-free graphs

For \(k\ge1\), put
\[
T_k=S_{1,1,k}.
\]
Thus \(T_k\) has a center, two arms of length \(1\), and one arm of length \(k\).

The key observation is that, in a \(T_k\)-free graph, an induced copy of \(T_{k-1}\) is a bounded-radius set.

## Lemma 3.1: bounded eccentricity of \(T_{k-1}\)

Let \(k\ge2\). If a connected \(T_k\)-free graph \(G\) contains an induced copy \(F\) of \(T_{k-1}\), then every vertex of \(G\) is at distance at most \(k\) from \(V(F)\).

### Proof

Label \(F\) as follows. Its center is \(c\), its two short leaves are \(a,b\), and its long arm is
\[
c-p_1-p_2-\cdots-p_{k-1}.
\]

Suppose, for a contradiction, that some vertex \(z\) has distance \(r\ge k+1\) from \(F\). Let
\[
q_1-q_2-\cdots-q_r=z
\]
be the portion outside \(F\) of a shortest \(F\)-to-\(z\) path. Then:

- \(A=N(q_1)\cap V(F)\) is nonempty;
- every \(q_i\), \(i\ge2\), is anticomplete to \(F\);
- \(q_1,\ldots,q_r\) induce a path.

If \(A\) is not a clique, choose nonadjacent \(u,w\in A\). Then
\[
q_1u,\quad q_1w,\quad
q_1-q_2-\cdots-q_{k+1}
\]
are respectively two arms of length \(1\) and one arm of length \(k\). There are no additional edges among these vertices, so they induce \(T_k\), a contradiction.

It remains to consider the case in which \(A\) is a clique. Since \(F\) is a tree, \(A\) is either a singleton or the two ends of an edge of \(F\). The possibilities are exhausted by the following table. In every row, the displayed long arm is continued along \(q_1,q_2,\ldots\) until it has exactly \(k\) edges.

\[
\begin{array}{c|c|c}
A & \text{two short leaves at }c & \text{beginning of the long arm}\\
\hline
\{c\} & a,b & c-q_1-\cdots\\
\{a\} & b,p_1 & c-a-q_1-\cdots\\
\{b\} & a,p_1 & c-b-q_1-\cdots\\
\{p_t\} & a,b & c-p_1-\cdots-p_t-q_1-\cdots\\
\{c,a\} & b,p_1 & c-q_1-\cdots\\
\{c,b\} & a,p_1 & c-q_1-\cdots\\
\{c,p_1\} & a,b & c-q_1-\cdots\\
\{p_t,p_{t+1}\} & a,b &
c-p_1-\cdots-p_t-q_1-\cdots
\end{array}
\]

Here \(1\le t\le k-1\) in the singleton row and \(1\le t\le k-2\) in the final row. Any second vertex of \(A\) not used in the displayed induced subgraph is simply omitted. Since \(q_i\), \(i\ge2\), is anticomplete to \(F\), and since \(q_1\) has no neighbors in \(F\setminus A\), every row indeed gives an induced \(T_k\). There are enough vertices on the \(q\)-path because \(r\ge k+1\).

This contradiction proves that every vertex is within distance \(k\) of \(F\). \(\square\)

For \(k=3\), this says:

> Every connected \(S_{1,1,3}\)-free graph is either \(S_{1,1,2}\)-free or has an induced \(S_{1,1,2}\) whose distance-\(3\) neighborhood is the whole graph.

## Corollary 3.2: a high-degree vertex

Let \(G\) be connected, \(T_k\)-free, and not \(T_{k-1}\)-free. If \(m=|V(G)|\) and \(\Delta=\Delta(G)\), then
\[
m\le C_k\max\{1,\Delta^k\},
\qquad
C_k=(k+2)(k+1).
\]

Indeed, \(T_{k-1}\) has \(k+2\) vertices, and by Lemma 3.1 its distance-\(k\) neighborhood covers \(G\). The number of vertices reachable from one root by walks of length at most \(k\) is at most
\[
1+\Delta+\cdots+\Delta^k
 \le (k+1)\max\{1,\Delta^k\}.
\]
Consequently, for all sufficiently large \(m\),
\[
\Delta(G)\ge \left(\frac{m}{C_k}\right)^{1/k}.
\]

## Theorem 3.3

For every fixed \(k\ge3\), Maximum Independent Set on \(T_k=S_{1,1,k}\)-free graphs can be solved in time
\[
2^{O_k(n^{1-1/k}\log n)}
   =n^{O_k(n^{1-1/k})}.
\]

### Algorithm

The proof is by induction on \(k\).

The base class \(T_2=S_{1,1,2}\)-free has a polynomial-time MIS algorithm by the premise of the catalog problem.

For \(k\ge3\), process connected components separately. On a connected \(T_k\)-free graph \(G\) with \(m\) vertices:

1. Test by brute force in \(m^{O(k)}\) time whether \(G\) contains an induced \(T_{k-1}\).
2. If it does not, invoke the algorithm for \(T_{k-1}\)-free graphs.
3. If it does, choose a maximum-degree vertex \(v\). By Corollary 3.2,
   \[
   \deg(v)\ge c_k m^{1/k}
   \]
   for a constant \(c_k>0\), apart from bounded-size instances.
4. Branch using
   \[
   \alpha(G)
   =\max\{\alpha(G-v),\,1+\alpha(G-N[v])\}.
   \]

Correctness follows directly from the branching identity and the induction hypothesis.

### Running time

At a branching node of size \(m\), the exclusion branch has size \(m-1\), while the inclusion branch has size at most
\[
m-c_km^{1/k}.
\]
Thus the relevant recurrence is
\[
R_k(m)
 \le R_k(m-1)
   +R_k(m-c_km^{1/k})
   +m^{O_k(1)}.
\]

Let
\[
p_k=1-\frac1k.
\]
The function
\[
F(m)=\exp\!\bigl(A m^{p_k}\log(m+2)\bigr)
\]
satisfies the recurrence for sufficiently large \(A=A(k)\). Indeed,
\[
m^{p_k}\log m-(m-1)^{p_k}\log(m-1)
   =\Theta(m^{-1/k}\log m),
\]
whereas
\[
m^{p_k}\log m
 -(m-c_km^{1/k})^{p_k}
       \log(m-c_km^{1/k})
   =\Theta(\log m).
\]
Hence the first child consumes a relative fraction
\(\Theta(m^{-1/k}\log m)\) of the available bound, while the second child is smaller by a factor \(m^{-\Theta(A)}\). Choosing \(A\) sufficiently large makes the latter smaller than the former slack. Polynomial work is also absorbed. A superadditive envelope of \(F\) handles the summation over connected components.

Finally,
\[
p_{k-1}=1-\frac1{k-1}<1-\frac1k=p_k,
\]
so the running time of the \(T_{k-1}\)-free subroutine is asymptotically absorbed by the claimed bound. This completes the induction. \(\square\)

In particular,
\[
\operatorname{MIS}(S_{1,1,3}\text{-free})
   \in 2^{O(n^{2/3}\log n)}.
\]

# 4. Why this does not settle \(S_{1,2,2}\)

The bounded-radius argument exploits the two arms of length \(1\). It does not extend directly to \(S_{1,2,2}\).

For example, consider \(S_{1,1,\ell}\) for arbitrarily large \(\ell\). It:

- contains \(S_{1,1,2}\);
- is \(S_{1,2,2}\)-free, because its unique degree-three vertex has only one arm of length at least \(2\);
- has maximum degree \(3\);
- has vertices arbitrarily far from every induced \(S_{1,1,2}\) centered at its degree-three vertex.

Thus an \(S_{1,2,2}\)-free graph that is not \(S_{1,1,2}\)-free need not have bounded radius or a high-degree vertex. The explicit induction above therefore gives no algorithm for that case.

Similarly, bounded diameter alone cannot resolve the problem: every connected \(P_7\)-free graph already has diameter at most \(5\), while polynomial-time MIS for \(P_7\)-free graphs remains open according to the supplied literature review.

# 5. Remaining gap

The results above establish:

\[
\boxed{
\forall H=S_{i,j,k}\text{ in the boundary},\ 
\forall\varepsilon>0,\ 
\operatorname{MIS}(H\text{-free})
\text{ has an exact }
2^{\varepsilon n}n^{O_{H,\varepsilon}(1)}
\text{ algorithm}.
}
\]

They also give a concrete single subexponential algorithm on the entire ray \(H=S_{1,1,k}\).

However, none of these bounds is polynomial, and subexponential-time solvability is compatible with NP-hardness in the absence of additional complexity assumptions. Therefore the requested standard complexity dichotomy—polynomial time versus NP-hardness—remains unresolved, in particular for \(P_7\), \(S_{1,1,3}\), and \(S_{1,2,2}\).