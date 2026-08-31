```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "I do not resolve the recursive exhaustion, but give exact quotient and dual formulations and, under the natural candidate hypotheses, prove that every non-diamond bichromatic-forbidding candidate has at least 13 vertices.",
  "would_publish": false,
  "caveats": "The prompt omits the formal definition of a 4-candidate and the three operations; the small-order theorem assumes the standard near-triangulation, degree, and no-separating-triangle hypotheses."
}
```

# Mathematical writeup

## 1. Status of the conjecture

Let the outer cycle be
\[
C=v_1v_2v_3v_4v_1.
\]
A bichromatic boundary coloring is a proper \(4\)-coloring \(\varphi\) satisfying
\[
\varphi(v_1)=\varphi(v_3),\qquad
\varphi(v_2)=\varphi(v_4).
\]
The conjecture asserts that every bichromatic-forbidding \(4\)-candidate belongs to the recursively generated class defined by Lemmas 27–29 of the source.

The supplied excerpt does not state the formal definition of a \(4\)-candidate or the three operations. Those details are indispensable for checking the exhaustion assertion: closure under the operations is not the difficult direction; one must prove that every non-diamond obstruction admits one of the corresponding inverse reductions. I therefore do not claim a proof or counterexample.

The following results are independent of those operations and give exact reformulations and a small-order structural result.

---

## 2. Identification reformulation

### Proposition 2.1

Let \(G\) be any graph with specified distinct vertices \(v_1,v_2,v_3,v_4\). Let \(Q(G)\) be the multigraph obtained by identifying
\[
v_1\sim v_3=:x,\qquad v_2\sim v_4=:y,
\]
retaining loops and parallel edges. Then \(G\) has a bichromatic boundary \(4\)-coloring if and only if \(Q(G)\) is \(4\)-colorable.

Consequently, \(G\) is bichromatic-forbidding if and only if \(Q(G)\) has no proper \(4\)-coloring.

#### Proof

A coloring of \(G\) constant on each of the two identified pairs descends to a coloring of \(Q(G)\). Conversely, a coloring of \(Q(G)\) pulls back to a coloring of \(G\) satisfying the two required equalities. Properness is preserved in both directions. If an identification creates a loop, both sides are automatically impossible. ∎

### Corollary 2.2

If \(Q(G)\) is loopless and \(G\) is bichromatic-forbidding, then the underlying simple graph of \(Q(G)\) contains a \(5\)-critical subgraph.

#### Proof

Choose an inclusion-minimal subgraph \(H\) of \(Q(G)\) which is not \(4\)-colorable. For every \(u\in V(H)\), \(H-u\) is \(4\)-colorable, and assigning a fifth color to \(u\) shows that \(\chi(H)=5\). Minimality also gives \(\delta(H)\ge4\). ∎

This is a useful way to search for counterexamples: after the two identifications, every chordless obstruction contains an ordinary \(5\)-critical core.

---

## 3. Dual \(3\)-edge-coloring formulation

Assume now that \(G\) is a plane near-triangulation whose outer face is \(C\). Let \(D=G^*\), including the dual vertex \(r\) corresponding to the outer face. Thus \(r\) has degree four and every other dual vertex has degree three.

Write the four colors as the elements of
\[
\Gamma=\mathbb Z_2^2.
\]
The three nonzero elements of \(\Gamma\) will be regarded as three edge colors.

### Proposition 3.1

Proper \(4\)-colorings of \(G\), modulo adding a fixed element of \(\Gamma\) to every vertex color, are in bijection with nowhere-zero \(\Gamma\)-flows on \(D\). At every cubic vertex of \(D\), the three incident edges receive the three distinct nonzero elements.

Under this bijection, the coloring of \(C\) is bichromatic if and only if all four edges incident with \(r\) receive the same nonzero value.

#### Proof

Given a proper coloring \(\varphi:V(G)\to\Gamma\), label the dual edge corresponding to \(uv\in E(G)\) by
\[
\lambda((uv)^*)=\varphi(u)+\varphi(v).
\]
This is nonzero because \(\varphi\) is proper. Around a triangular face \(uvw\),
\[
\lambda(uv)+\lambda(vw)+\lambda(wu)=0.
\]
Three nonzero elements of \(\Gamma\) sum to zero precisely when they are the three distinct nonzero elements. Thus conservation holds at every cubic dual vertex; conservation at \(r\) follows by summing around the outer boundary.

Conversely, identify a nowhere-zero dual flow with labels on primal edges. Conservation around every face says that the sum of labels around each facial boundary is zero. Facial cycles span the binary cycle space, so the sum around every primal cycle is zero. Fix a root \(s\) and define \(\varphi(v)\) as the sum of edge labels along any \(s\)-\(v\) path. This is path-independent and gives a proper coloring. It is unique up to translating all colors.

Finally, if \(v_i v_{i+1}\) are indexed cyclically, then a bichromatic boundary coloring has the form
\[
a,b,a,b,
\]
so every boundary-edge difference is \(a+b\). Conversely, if all four boundary-edge differences equal \(x\ne0\), integration around \(C\) gives
\[
a,a+x,a,a+x.
\]
∎

At \(r\), conservation implies that the multiplicity of each of the three dual colors is even. Hence every possible boundary state is either

* monochromatic: \(4+0+0\), or
* of type \(2+2+0\).

Thus bichromatic-forbidding is exactly the assertion that the associated planar cubic \(4\)-pole has no monochromatic boundary state. This converts the conjecture into a finite-state decomposition problem for planar \(4\)-poles.

---

## 4. A Kempe-locking condition

Put a new vertex \(z\) in the outer face of \(G\) and join it to all four vertices of \(C\). Denote the resulting plane graph by \(\widehat G\).

A bichromatic coloring of \(G\) extends to \(\widehat G\), since two colors remain available for \(z\). Conversely, restriction of such a coloring of \(\widehat G\) gives a bichromatic coloring of \(G\).

Assume \(C\) has no chord and \(\widehat G\) is a plane triangulation. By the Four Color Theorem, \(\widehat G\) has a proper \(4\)-coloring. If \(G\) is bichromatic-forbidding, then every coloring of \(\widehat G\) uses exactly three colors on \(C\): four are impossible because \(z\) needs a color, and two are forbidden.

### Proposition 4.1

Suppose \(G\) is bichromatic-forbidding and \(\varphi\) is a coloring of \(\widehat G\) such that
\[
\varphi(v_1)=\varphi(v_3)=\alpha,\qquad
\varphi(v_2)=\beta,\qquad
\varphi(v_4)=\gamma,
\]
where \(\alpha,\beta,\gamma\) are distinct. Then \(v_2\) and \(v_4\) lie in the same component of the \((\beta,\gamma)\)-Kempe subgraph.

#### Proof

Otherwise interchange \(\beta\) and \(\gamma\) on the component containing \(v_4\). This preserves properness and leaves \(v_2\) unchanged. After the interchange,
\[
\varphi(v_1)=\varphi(v_3),\qquad
\varphi(v_2)=\varphi(v_4),
\]
contradicting the bichromatic-forbidding property. ∎

Topologically, such a \(v_2\)-\(v_4\) Kempe path separates \(v_1\) from \(v_3\) in the disk. Any proof by inverse reductions must exploit these forced Kempe separators strongly enough to recover one of the three source operations.

---

## 5. A hand-verifiable small-order result

This section uses the following standard candidate-patch hypotheses:

1. \(G\) is a finite simple plane near-triangulation with outer boundary \(C=v_1v_2v_3v_4v_1\);
2. every interior vertex has degree at least five;
3. every boundary vertex has degree at least four;
4. \(G\) has no separating triangle.

These are the natural hypotheses obtained by deleting the crossing region from an edge-maximal one-crossing graph of minimum degree five. If the source definition does not imply all four conditions, the result below applies only to this subclass.

### Theorem 5.1

Under the preceding hypotheses:

1. if \(C\) has a chord, then \(G\) is the diamond;
2. if \(C\) is chordless, then \(|V(G)|\ge12\);
3. the unique chordless example with \(|V(G)|=12\) is the icosahedral graph with one edge deleted, with the resulting quadrilateral as outer face;
4. this \(12\)-vertex graph has a bichromatic boundary coloring.

Consequently, every bichromatic-forbidding graph satisfying these candidate hypotheses is either the exceptional diamond or has at least \(13\) vertices.

### Proof

#### Step 1: Chords

Suppose \(v_1v_3\in E(G)\). The two triangles
\[
v_1v_2v_3,\qquad v_1v_3v_4
\]
partition the disk bounded by \(C\). If either contains a vertex, it is a separating triangle. Hence both are facial and \(G\) is exactly \(K_4\) minus the edge \(v_2v_4\), namely the diamond.

Henceforth assume \(C\) is chordless.

#### Step 2: Capping the patch

Add a vertex \(z\) on the other side of \(C\), adjacent to all four vertices of \(C\). The resulting graph \(T\) is a simple plane triangulation with no separating triangle. Moreover,
\[
d_T(z)=4,\qquad d_T(v)\ge5\quad(v\ne z).
\]

Let \(N=|V(T)|=|V(G)|+1\), and for \(v\ne z\) put
\[
\varepsilon(v)=d_T(v)-5\ge0,\qquad
E=\sum_{v\ne z}\varepsilon(v).
\]
For every plane triangulation,
\[
\sum_{v\in V(T)}(6-d_T(v))=12.
\]
Therefore
\[
12=2+\sum_{v\ne z}(1-\varepsilon(v))
   =2+(N-1)-E,
\]
and hence
\[
E=N-11. \tag{5.1}
\]
In particular \(N\ge11\).

#### Step 3: The first layer around \(C\)

Write \(C=a_1a_2a_3a_4a_1\), and let
\[
S=\sum_{i=1}^4\varepsilon(a_i).
\]
On the side of \(C\) not containing \(z\), the vertex \(a_i\) has
\[
2+\varepsilon(a_i)
\]
neighbors. Let \(x_i\) be the third vertex of the triangular face incident with \(a_i a_{i+1}\) on this side.

The interior neighbors of \(a_i\), in order, form a path from \(x_{i-1}\) to \(x_i\), containing \(\varepsilon(a_i)\) intermediate vertices. For \(E\le2\), these paths concatenate to a simple cycle \(W\) of length
\[
|W|=4+S.
\]
Indeed:

* adjacent face-apices cannot coincide, since that would leave only one neighbor in the corresponding sector;
* opposite face-apices cannot coincide, since the common vertex would create a nonfacial triangle with an intervening boundary edge;
* an intermediate vertex cannot coincide with an apex or with an intermediate vertex at an adjacent boundary corner, again because this creates a nonfacial triangle;
* if one intermediate vertex occurred at two opposite corners, then \(S=E=2\), while that vertex would have at least six neighbors, forcing one additional unit of excess, a contradiction.

The annulus between \(C\) and \(W\) is triangulated. There are exactly
\[
8+S
\]
edges between \(C\) and \(W\): the four \(x_i\) have two boundary neighbors each, while every intermediate vertex has one.

Let \(Y\) be the set of vertices strictly inside \(W\), let \(r=|Y|\), and let \(q\) be the number of edges between \(W\) and \(Y\). Put
\[
E_W=\sum_{w\in W}\varepsilon(w).
\]
If \(c\) denotes the number of chords of \(W\), degree counting on \(W\) gives
\[
\begin{aligned}
q
 &=5|W|+E_W-(8+S)-2(|W|+c)\\
 &=4+2S+E_W-2c\\
 &\le 4+2S+(E-S)=4+S+E. \tag{5.2}
\end{aligned}
\]

All neighbors of a vertex in \(Y\) belong to \(Y\cup W\). Thus, writing \(e(Y)\) for the number of edges induced by \(Y\),
\[
q=\sum_{y\in Y}d_T(y)-2e(Y)\ge 5r-2\binom r2. \tag{5.3}
\]

For \(N\le13\), the possibilities are:

\[
\begin{array}{c|c|c|c|c|c}
N&E&S&r=N-9-S&\text{upper bound on }q&\text{lower bound on }q\\
\hline
11&0&0&2&4&8\\
12&1&0&3&5&9\\
12&1&1&2&6&8\\
13&2&0&4&6&8\\
13&2&1&3&7&9\\
13&2&2&2&8&8
\end{array}
\]

All rows except the last are impossible. Therefore \(N\ge13\), proving
\[
|V(G)|=N-1\ge12.
\]

#### Step 4: Equality when \(N=13\)

Suppose \(N=13\). Equality throughout the last row implies:

* \(S=2\);
* \(W\) is a chordless \(6\)-cycle;
* all vertices of \(W\cup Y\) have degree five;
* \(Y=\{y,y'\}\), with \(yy'\in E(T)\);
* there are eight edges between \(W\) and \(Y\);
* four vertices of \(W\) have one neighbor in \(Y\), while the two intermediate fan vertices have two neighbors in \(Y\).

Thus both intermediate vertices are common neighbors of \(y\) and \(y'\). The two facial triangles incident with \(yy'\) show that these common neighbors divide \(W\) into two arcs. Since each of \(y,y'\) has four neighbors on \(W\), both arcs have length three. Hence the two intermediate vertices are opposite on \(W\).

This is possible only when the two units of boundary excess occur at opposite vertices of \(C\), one unit at each. Thus two opposite vertices of \(C\) have degree six in \(T\), while the other two have degree five.

Delete \(z\) and add the diagonal joining the two degree-five vertices of \(C\). The resulting graph \(H\) is a simple plane triangulation on twelve vertices, all of degree five.

#### Step 5: The only \(5\)-regular triangulation on twelve vertices

First, \(H\) has no separating triangle. If a separating triangle has \(k\) vertices on one side, then in the corresponding triangulated disk the \(k\) interior vertices all have degree five. If \(e_0\) is the number of edges among these \(k\) vertices and \(t\) the number of edges from them to the boundary triangle, then
\[
e_0+t=3k,\qquad 2e_0+t=5k,
\]
so \(e_0=2k\). For \(1\le k\le5\), this is impossible for a simple planar graph on \(k\) vertices. Therefore each side of a separating triangle would contain at least six vertices, whereas only nine vertices lie outside the triangle.

Now choose a vertex \(u\) of \(H\). Its five neighbors \(a_0,\dots,a_4\) form an induced \(5\)-cycle. For each edge \(a_i a_{i+1}\), let \(b_i\) be the third vertex of the face on the side away from \(u\). Degree five and the absence of separating triangles imply that the five \(b_i\) are distinct and form another \(5\)-cycle.

There is one remaining vertex \(v\). Each \(b_i\) already has four known neighbors:
\[
a_i,\ a_{i+1},\ b_{i-1},\ b_{i+1}.
\]
The region bounded by the \(b_i\)-cycle contains only \(v\). If \(t\) is the number of \(b_i v\) edges and \(c\) the number of chords of that \(5\)-cycle, triangulation gives
\[
t+c=5,
\]
while the five remaining degree slots at the \(b_i\)'s give
\[
t+2c=5.
\]
Hence \(c=0\) and \(t=5\). This is precisely the icosahedral graph.

It follows that \(G\) is the icosahedral graph with one edge deleted.

#### Step 6: An explicit bichromatic coloring

Represent the icosahedron by vertices
\[
u,\ v,\ a_0,\ldots,a_4,\ b_0,\ldots,b_4
\]
with indices modulo five and edges

* \(ua_i\) and \(vb_i\) for all \(i\);
* \(a_i a_{i+1}\) and \(b_i b_{i+1}\);
* \(a_i b_i\) and \(a_i b_{i-1}\).

Delete the edge \(ua_1\). Its two incident triangles merge into the outer \(4\)-face
\[
u\,a_0\,a_1\,a_2\,u.
\]
The following color classes give a proper \(4\)-coloring:
\[
\begin{aligned}
1&:\{u,a_1,b_3\},\\
2&:\{a_0,a_2,v\},\\
3&:\{a_3,b_1,b_4\},\\
4&:\{a_4,b_0,b_2\}.
\end{aligned}
\]
On the outer cycle the colors are
\[
1,2,1,2.
\]
Thus this unique \(12\)-vertex candidate is not bichromatic-forbidding. ∎

---

## 6. A fully specified computational test

For any fixed near-triangulation \(G\), Proposition 3.1 yields a particularly small SAT instance.

Construct \(D=G^*\), with degree-four outer dual vertex \(r\). For every dual edge \(e\) and every \(c\in\{1,2,3\}\), introduce a variable \(X_{e,c}\).

Impose:

1. exactly one \(X_{e,c}\) is true for each edge \(e\);
2. at each cubic vertex, its three incident edges have pairwise different labels;
3. all four edges incident with \(r\) have label \(1\).

The instance is satisfiable exactly when \(G\) admits a bichromatic boundary coloring. Color \(1\) can be fixed without loss of generality because the three nonzero elements of \(\mathbb Z_2^2\) are symmetric. An UNSAT certificate therefore certifies that \(G\) is bichromatic-forbidding.

To test Conjecture 30 up to an order bound, one would additionally:

1. enumerate the relevant embedded \(4\)-candidates canonically;
2. retain precisely the SAT-UNSAT instances;
3. recursively search for inverse occurrences of the operations in Lemmas 27–29;
4. canonically memoize all reduced plane maps.

A counterexample certificate should contain the rotation system, the candidate-condition checks, an UNSAT proof for the preceding instance, and a check that none of the three inverse operations applies. No such computation is claimed here.

---

## 7. Remaining gap

The exact obstruction is now expressible in three equivalent ways:

1. \(Q(G)\) is not \(4\)-colorable;
2. the dual cubic \(4\)-pole has no monochromatic boundary state;
3. every cap coloring is Kempe-locked across its unequal opposite pair.

What is still missing is the central recursive statement: from one of these global obstructions, deduce a local or separating configuration that is exactly the inverse of one of Lemmas 27–29. The forced Kempe path need not by itself have a canonical local form, and the dual state condition alone does not rule out an internally irreducible \(4\)-pole. Thus the argument above neither proves exhaustion nor supplies a counterexample.