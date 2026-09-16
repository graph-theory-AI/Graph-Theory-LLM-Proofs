```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Graceful-labeling search has a one-sided randomized n^{O(k)} algorithm for trees with k non-leaf vertices, via an exact leaf-completion criterion.",
  "would_publish": false,
  "caveats": "This is an algorithmic partial result, not a general existence proof; novelty is not established."
}
```

## 1. Result and scope

I do not prove or disprove the Graceful Tree Conjecture. The rigorous outcome here is a parameterized search algorithm: after fixing the labels of the non-leaf vertices, completing the labeling reduces to a precisely specified colored-matching problem.

I use the standard definition: a graceful labeling of an \(n\)-vertex tree is a **bijection**
\[
f:V(T)\longrightarrow\{0,\ldots,n-1\}
\]
whose edge differences are exactly \(1,\ldots,n-1\).

### Theorem
Let \(T\) be an \(n\)-vertex tree, and let
\[
k=\bigl|\{v\in V(T):\deg_T(v)\ge 2\}\bigr|.
\]
There is a randomized algorithm with the following properties:

1. It outputs either a graceful labeling of \(T\) or `FAIL`.
2. It never outputs an incorrect labeling.
3. If \(T\) is graceful, it outputs a graceful labeling with probability greater than \(1/2\).
4. If \(T\) is not graceful, it always outputs `FAIL`.
5. For \(n\ge3\), one run uses \(O(n^{2k+3})\) operations over a finite field of order \(O(n)\), and polynomial space.

Thus, for every fixed \(k\), this is a one-sided randomized polynomial-time search algorithm. Independent repetition \(r\) times reduces the failure probability on graceful trees to at most \(2^{-r}\).

This is an XP-type bound, not an FPT bound. I do not claim that this formulation is new.

## 2. Freezing the non-leaf labels

The cases \(n=1,2\) have immediate graceful labelings, so assume \(n\ge3\).

Put
\[
C=\{v:\deg_T(v)\ge2\}=\{v_1,\ldots,v_k\},
\qquad
L=V(T)\setminus C,
\qquad
\ell=|L|=n-k.
\]
Every vertex of \(L\) is a leaf whose neighbor lies in \(C\). Define
\[
b_i=|N_T(v_i)\cap L|,
\qquad
\sum_{i=1}^k b_i=\ell.
\]
There are exactly \(k-1\) edges inside \(C\).

Fix an injective assignment
\[
a_i\in\{0,\ldots,n-1\}\qquad(1\le i\le k)
\]
to the vertices of \(C\). Reject this assignment if two edges inside \(C\) have the same difference.

For an assignment not rejected, let
\[
U=\{0,\ldots,n-1\}\setminus\{a_1,\ldots,a_k\}
\]
be the unused vertex labels, and let
\[
D=\{1,\ldots,n-1\}
 \setminus
 \{|a_i-a_j|:v_iv_j\in E(T[C])\}
\]
be the unused edge differences. Both sets have cardinality \(\ell\).

Construct a bipartite **multigraph** \(B_{\mathbf a}\) with parts \(U\) and \(D\). For every \(x\in U\) and every \(i\), include an edge
\[
(x,d,i),\qquad d=|x-a_i|,
\]
provided \(d\in D\). Give this edge color \(i\).

Parallel edges of different colors are retained.

### Leaf-completion criterion
The fixed assignment \(\mathbf a=(a_1,\ldots,a_k)\) extends to a graceful labeling of \(T\) if and only if \(B_{\mathbf a}\) has a perfect matching containing exactly \(b_i\) edges of color \(i\), for every \(i\).

#### Proof

Suppose a graceful completion exists. A leaf labeled \(x\), adjacent to \(v_i\), produces the edge difference \(d=|x-a_i|\). Select the corresponding edge \((x,d,i)\) of \(B_{\mathbf a}\).

Every unused vertex label occurs once, every unused difference occurs once, and exactly \(b_i\) leaves are adjacent to \(v_i\). Hence the selected edges form the required perfect matching.

Conversely, suppose such a perfect matching exists. For each \(i\), assign the labels on its \(b_i\) color-\(i\) matching edges bijectively to the \(b_i\) leaves adjacent to \(v_i\). All labels in \(U\) are used once, and the resulting leaf-edge differences are exactly \(D\). Together with the fixed core labels and differences, this gives a graceful labeling. \(\square\)

All differences here are ordinary integer differences. The finite field introduced below is only an algorithmic device.

## 3. An exact algebraic test for completion

Introduce a separate indeterminate \(w_e\) for every colored edge \(e\) of \(B_{\mathbf a}\), and variables \(z_1,\ldots,z_k\).

Form the \(\ell\times\ell\) matrix \(H\), with rows indexed by \(U\) and columns by \(D\), where
\[
H_{x,d}
=
\sum_{\substack{1\le i\le k\\ |x-a_i|=d}}
w_{(x,d,i)}z_i.
\]
Define
\[
P_{\mathbf a}(\mathbf w)
=
[z_1^{b_1}\cdots z_k^{b_k}]\det H.
\]

### Algebraic criterion
Over any field,
\[
P_{\mathbf a}\not\equiv0
\quad\Longleftrightarrow\quad
\mathbf a\text{ has a graceful completion}.
\]

#### Proof

Expanding the determinant gives a sum over perfect matchings of the colored multigraph. A matching \(M\) contributes
\[
\operatorname{sgn}(M)
\left(\prod_{e\in M}w_e\right)
\prod_{i=1}^k z_i^{c_i(M)},
\]
where \(c_i(M)\) counts its color-\(i\) edges.

Consequently, \(P_{\mathbf a}\) is the signed sum of the monomials
\[
\prod_{e\in M}w_e
\]
over precisely the perfect matchings having the required color counts.

Crucially, distinct colored matchings give distinct monomials in the individually indexed variables \(w_e\). Thus these terms cannot cancel identically. Each has coefficient \(1\) or \(-1\), which is nonzero over any field.

The conclusion now follows from the leaf-completion criterion. \(\square\)

The separate edge variables are essential: substituting all \(w_e=1\) at the outset would allow determinant cancellation and would not be an exact existence test.

## 4. Randomized evaluation in \(n^{O(k)}\) time

### 4.1 Random substitution

Let \(s\) be the least power of two strictly greater than \(2n\), and choose a prime
\[
s<p<2s.
\]
Such a prime exists by Bertrand’s postulate. In particular, \(p=O(n)\).

Work over \(\mathbb F_p\), and sample every \(w_e\) independently and uniformly from
\[
S=\{0,\ldots,s-1\}\subset\mathbb F_p.
\]
This uses a fixed number of fair random bits per weight.

Every monomial of \(P_{\mathbf a}\) has degree \(\ell\). The elementary polynomial zero bound therefore gives, whenever \(P_{\mathbf a}\not\equiv0\),
\[
\Pr\bigl(P_{\mathbf a}(\mathbf w)=0\bigr)
\le \frac{\ell}{s}<\frac12.
\]

For completeness, this bound follows by induction on the number of variables. If the degree in the last variable is \(d\), its leading coefficient has total degree at most \(\ell-d\). The probability that this coefficient vanishes is at most \((\ell-d)/|S|\); otherwise the resulting univariate polynomial has at most \(d\) roots in \(S\).

A nonzero evaluation is therefore a valid certificate that a graceful completion exists. A zero evaluation is inconclusive.

### 4.2 Computing the coefficient

It remains important that we can compute the evaluated coefficient without expanding the determinant into \(\ell!\) terms.

The determinant is homogeneous of total degree \(\ell\) in the \(z_i\), and \(\sum_i b_i=\ell\). Hence
\[
P_{\mathbf a}(\mathbf w)
=
[z_1^{b_1}\cdots z_{k-1}^{b_{k-1}}]
\det H(z_1,\ldots,z_{k-1},1;\mathbf w).
\]
Setting \(z_k=1\) loses no information about the desired coefficient: its exponent is forced by total degree.

The polynomial on the right has degree at most \(\ell\) in each remaining variable. Evaluate it on
\[
\{0,1,\ldots,\ell\}^{k-1}
\]
and extract the desired coefficient by ordinary multivariate interpolation. These evaluation points are distinct in \(\mathbb F_p\).

There are
\[
(\ell+1)^{k-1}\le n^{k-1}
\]
grid points. Each determinant can be evaluated by Gaussian elimination in \(O(n^3)\) field operations. Thus one coefficient test costs
\[
O(n^{k+2})
\]
field operations, including polynomial-size interpolation preprocessing.

The interpolation sum can be streamed: there is no need to retain all grid evaluations.

### 4.3 Enumerating the core assignments

The algorithm enumerates all injective assignments
\[
\mathbf a:C\longrightarrow\{0,\ldots,n-1\}.
\]
There are at most \(n^k\) of them. For each assignment:

1. Reject repeated core-edge differences.
2. Construct \(B_{\mathbf a}\).
3. Sample the edge weights.
4. Evaluate \(P_{\mathbf a}\).
5. If the result is nonzero, recover a completion as described next.

If all assignments have been exhausted, return `FAIL`.

If \(T\) is not graceful, every coefficient polynomial is identically zero, so there are no false positives.

If \(T\) is graceful, fix one graceful labeling and let \(\mathbf a^\ast\) be its restriction to \(C\). Then
\[
P_{\mathbf a^\ast}\not\equiv0.
\]
The algorithm succeeds either before reaching this assignment or when this assignment has a nonzero evaluation. Its failure probability is consequently less than \(1/2\).

There is **no union-bound penalty involving the \(n^k\) assignments**: it suffices to consider one fixed assignment that has a completion.

## 5. Recovering an actual graceful labeling

A nonzero evaluated coefficient also permits deterministic extraction of a suitable matching, using the same fixed weights.

Choose any remaining row \(x\). Laplace expansion along that row gives
\[
P_{\mathbf b}
=
\sum_{e=(x,d,i)}
\sigma_e w_e\,
P^{\,x,d}_{\mathbf b-\mathbf e_i},
\]
where:

- \(\sigma_e\in\{1,-1\}\) is the cofactor sign;
- \(P^{\,x,d}\) is the corresponding coefficient for the matrix with row \(x\) and column \(d\) deleted;
- a coefficient with a negative target exponent is interpreted as zero.

If the left side is nonzero, at least one summand is nonzero. Test the candidate edges, select one with
\[
w_e P^{\,x,d}_{\mathbf b-\mathbf e_i}\ne0,
\]
delete its row and column, and decrease \(b_i\) by one.

This preserves a nonzero coefficient for the smaller instance. Repetition reaches the empty matrix and produces a perfect matching with exactly the prescribed color counts. The leaf-completion criterion then constructs the graceful labeling explicitly.

Every row has at most \(k\) colored edges. Thus extraction uses at most \(k\ell\) additional coefficient tests. The enumeration costs
\[
O(n^k n^{k+2})=O(n^{2k+2}),
\]
and extraction costs at most
\[
O(k n^{k+3})=O(n^{2k+3}).
\]
This proves the stated overall bound.

The graph weights, current matrix, interpolation data, and enumeration counters can all be stored in polynomial space. Field elements have \(O(\log n)\) bits, so the bit complexity differs only by polylogarithmic factors.

This completes the proof of the theorem.

## 6. Why this does not prove the conjecture

The completion criterion is not automatically satisfied by an assignment with distinct core labels and distinct core-edge differences.

For example, consider the path
\[
a-v-w-b
\]
and fix
\[
f(v)=0,\qquad f(w)=3.
\]
The core difference is \(3\), leaving
\[
U=D=\{1,2\}.
\]
We need one leaf edge of each core color. The matrix has the form
\[
H=
\begin{pmatrix}
\alpha z_v & \beta z_w\\
\gamma z_w & \delta z_v
\end{pmatrix},
\]
so
\[
\det H=\alpha\delta z_v^2-\beta\gamma z_w^2.
\]
The required coefficient of \(z_vz_w\) is identically zero. This particular core assignment cannot be completed.

The tree itself is, of course, graceful:
\[
(f(a),f(v),f(w),f(b))=(1,2,0,3)
\]
gives edge differences \(1,2,3\). Thus the obstruction concerns the chosen core assignment, not the conjecture.

The argument above establishes an exact completion criterion and a randomized search bound. It does **not** establish that some coefficient polynomial is nonzero for every tree. Also, a randomized `FAIL` is not a certificate of a counterexample. No additional computational verification of cases, or advance over the literature’s existence results, is claimed.