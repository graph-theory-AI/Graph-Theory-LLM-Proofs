```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the sharp bound 7 for partial 2-trees and a planar obstruction to coarsening the standard 80-label construction, without determining the planar maximum.",
  "would_publish": false,
  "caveats": "The supplied interval [18,80] is unchanged; novelty of the partial results is not claimed."
}
```

# Scope of the result

Let
\[
M=\max\{\chi_o(D):D\text{ is an orientation of a planar graph}\}.
\]
I do **not** determine \(M\), or improve the bounds \(18\le M\le80\) reported in the question.

The partial results below are:

1. A self-contained proof that the maximum is exactly \(7\) for partial \(2\)-trees.
2. An obstruction to one natural attack on the upper bound \(80\): even on a connected, bipartite, planar graph of treewidth two, every colouring obtained from a particular acyclic five-colouring by the standard parity construction can be impossible to coarsen below \(80\). This holds even though the graph itself is \(7\)-colourable.

The second statement distinguishes an inefficient colouring construction from the actual oriented chromatic number.

Throughout, oriented colouring means homomorphism to a tournament, as in the question. In particular, adjacent vertices receive different colours. Also, the endpoints of a directed two-edge path receive different colours: identifying the endpoints would create a loop or a pair of opposite arcs in the target.

# 1. A sharp planar subclass: partial \(2\)-trees

A \(2\)-tree starts with an edge and repeatedly adds a vertex adjacent to both ends of an existing edge. A partial \(2\)-tree is a subgraph of a \(2\)-tree; equivalently, it has treewidth at most two.

## Proposition 1
Every oriented partial \(2\)-tree has oriented chromatic number at most \(7\), and this bound is attained by an oriented outerplanar graph.

### The seven-vertex target

Let \(Q\) be the tournament on \(\mathbb Z_7\) with
\[
x\longrightarrow y
\quad\Longleftrightarrow\quad
y-x\in\{1,2,4\}.
\]
For every pair of distinct vertices \(x,y\), and every prescription of the directions between a new vertex and \(x,y\), there is a vertex of \(Q\) realizing that prescription.

To verify this, translations and multiplication by elements of \(\{1,2,4\}\) are automorphisms of \(Q\). Thus any arc can be normalized to \(0\to1\). Writing \(N^+(x)\) and \(N^-(x)\) for out- and in-neighbourhoods, respectively, the four possibilities are
\[
\begin{array}{c|c}
\text{Prescribed neighbourhood} & \text{Available vertices}\\ \hline
N^+(0)\cap N^+(1)&\{2\}\\
N^+(0)\cap N^-(1)&\{4\}\\
N^-(0)\cap N^+(1)&\{3,5\}\\
N^-(0)\cap N^-(1)&\{6\}.
\end{array}
\]
Every set is nonempty.

Now complete the underlying partial \(2\)-tree to a \(2\)-tree, orienting added edges arbitrarily. Map its initial edge to an arc of \(Q\). At each subsequent step, the new vertex has two earlier neighbours that are adjacent, so their images are distinct. The displayed extension property supplies an image for the new vertex, whatever its two incident arc directions are. Restricting the resulting homomorphism proves the upper bound.

### Sharpness

Take a fan with centre \(z\) and path vertices \(v_1,\ldots,v_6\). Orient
\[
v_1\to v_2\to\cdots\to v_6,
\]
and orient the spokes by
\[
z\to v_1,v_2,v_3,
\qquad
v_4,v_5,v_6\to z.
\]

Every pair of vertices is adjacent or is joined by a directed two-edge path:

- within either triple \(\{v_1,v_2,v_3\}\) or \(\{v_4,v_5,v_6\}\), use the directed path;
- between the two triples, use \(v_j\to z\to v_i\), where \(j\ge4\) and \(i\le3\);
- \(z\) is adjacent to every other vertex.

Consequently every homomorphism to a tournament is injective on these seven vertices. The fan is outerplanar and is itself a \(2\)-tree. Thus the bound is sharp. \(\square\)

# 2. The standard acyclic-colouring target

Here is the \(80\)-label construction in a form suitable for examining possible improvements.

For \(r\ge2\), define an oriented graph \(Z_r\) with vertex set
\[
V(Z_r)=
\left\{(i,\mathbf b):
i\in[r],\
\mathbf b\in\{0,1\}^{[r]\setminus\{i\}}
\right\}.
\]
There are \(r2^{r-1}\) vertices. There are no arcs within one first-coordinate class. For \(i<j\), put
\[
(i,\mathbf b)\to(j,\mathbf d)
\quad\Longleftrightarrow\quad
b_j\oplus d_i=0,
\tag{1}
\]
and put the opposite arc otherwise.

Suppose \(\varphi:V(D)\to[r]\) is an acyclic proper colouring of the underlying graph. For an edge whose endpoints have colours \(i<j\), let
\[
\epsilon(e)=
\begin{cases}
0,&\text{if its arc goes from colour }i\text{ to colour }j,\\
1,&\text{otherwise}.
\end{cases}
\]
Choose bits satisfying
\[
b_j(u)\oplus b_i(v)=\epsilon(uv)
\qquad
\bigl(\varphi(u)=i,\ \varphi(v)=j\bigr).
\tag{2}
\]

For each colour pair, these equations are on a forest. Choose one bit in each component and propagate along its edges. Different colour pairs use different coordinates, so there is no compatibility issue between their systems.

The map
\[
v\longmapsto \bigl(\varphi(v),\mathbf b(v)\bigr)
\]
is then a homomorphism to \(Z_r\). Completing \(Z_r\) to a tournament gives
\[
\chi_o(D)\le r2^{r-1}.
\]
With the acyclic five-colourability theorem quoted in the question, this gives \(80\).

## Proposition 2
\[
\chi_o(Z_r)=r2^{r-1}.
\]

### Proof

Vertices in different first-coordinate classes are adjacent.

Consider distinct vertices \((i,\mathbf b)\) and \((i,\mathbf d)\) in the same class. Choose \(j\) with \(b_j\ne d_j\). For any vertex \(w\) in class \(j\), equation (1) makes its incidences with these two vertices oppositely directed. Hence they are the endpoints of a directed two-edge path through \(w\).

Thus every two vertices of \(Z_r\) must receive distinct colours. \(\square\)

This already rules out improving \(80\) by taking a homomorphic quotient of the entire standard target. The next construction makes the obstruction stronger: all its arcs can be forced into the colour image of a planar graph, regardless of the component-bit choices in (2).

# 3. A planar obstruction to coarsening the construction

## Theorem 3
There exists a connected bipartite planar oriented graph \(D\), with treewidth at most two, and an acyclic five-colouring \(\varphi\), such that:

1. \(\chi_o(D)\le7\);
2. every homomorphism
   \[
   c:D\to Z_5
   \]
   whose first coordinate is \(\varphi\) has arc image equal to all of \(Z_5\);
3. consequently, every coarsening of such a colouring that is still an oriented colouring uses at least \(80\) colours.

One explicit construction has \(20\,411\) vertices.

The phrase “coarsening” is important: each old colour class must remain monochromatic. The theorem does not prohibit a completely different colouring with seven colours.

## 3.1. A piece for one colour pair

Fix \(i<j\) in \([5]\). Write
\[
\mathcal B_i=\{0,1\}^{[5]\setminus\{i\}},
\qquad
\mathcal B_j=\{0,1\}^{[5]\setminus\{j\}}.
\]
Enumerate all \(256\) pairs in \(\mathcal B_i\times\mathcal B_j\) as
\[
(\mathbf p_t,\mathbf q_t),\qquad 0\le t<m,\quad m=256,
\]
in lexicographic order. In particular, \(\mathbf p_0=\mathbf q_0=\mathbf0\).

Construct a graph \(L_{ij}\) as follows.

- Introduce \(x_t,y_t\) for \(0\le t<m\), with
  \[
  \varphi(x_t)=i,\qquad \varphi(y_t)=j.
  \]
- Add the main path
  \[
  x_0y_0x_1y_1\cdots x_{m-1}y_{m-1}.
  \]
- For each \(0\le t<m-1\) and each \(h\notin\{i,j\}\), introduce:
  - \(u_{t,h}\), adjacent to \(x_t,x_{t+1}\);
  - \(v_{t,h}\), adjacent to \(y_t,y_{t+1}\);
  
  and give both new vertices colour \(h\).

### Planarity and treewidth

Temporarily add all edges \(x_tx_{t+1}\) and \(y_ty_{t+1}\). The graph on the \(x\)'s and \(y\)'s is a \(2\)-tree: start with \(x_0y_0\), and successively add
\[
x_{t+1}\text{ on }x_ty_t,
\qquad
y_{t+1}\text{ on }x_{t+1}y_t.
\]
Each \(u_{t,h}\) or \(v_{t,h}\) can then be added on its corresponding added edge. Deleting those temporary edges gives \(L_{ij}\). Hence \(L_{ij}\) is a partial \(2\)-tree.

It is also bipartite, with parts
\[
\{x_t\}\cup\{v_{t,h}\}
\quad\text{and}\quad
\{y_t\}\cup\{u_{t,h}\}.
\]

### Acyclicity of \(\varphi\)

All colour-pair cases are explicit:

- colours \(i,j\) induce the main path;
- colours \(i,h\) induce the subdivided \(x\)-chain, together with isolated vertices;
- colours \(j,h\) induce the subdivided \(y\)-chain, together with isolated vertices;
- two colours outside \(\{i,j\}\) induce an independent set.

Thus \(\varphi\) is an acyclic five-colouring.

## 3.2. Orienting the piece

Assign prototype bit vectors \(\boldsymbol\beta\) by
\[
\boldsymbol\beta(x_t)=\mathbf p_t,
\qquad
\boldsymbol\beta(y_t)=\mathbf q_t.
\]
For helper vertices, prescribe
\[
\beta_i(u_{t,h})=(\mathbf p_t)_h,
\qquad
\beta_j(v_{t,h})=(\mathbf q_t)_h,
\]
and set every unspecified coordinate to zero.

Orient every edge so that
\[
v\longmapsto
\bigl(\varphi(v),\boldsymbol\beta(v)\bigr)
\]
is a homomorphism to \(Z_5\). This specifies a unique direction for each edge, because its endpoints have different first coordinates and \(Z_5\) has exactly one arc between their labels.

## 3.3. Every permitted bit assignment covers all label pairs

Consider any other homomorphism to \(Z_5\) respecting \(\varphi\), and denote its bit vectors by \(\mathbf b(v)\).

For a coordinate \(k\ne\varphi(v)\), put
\[
d_k(v)=b_k(v)\oplus\beta_k(v).
\]
Subtracting the two instances of (2) shows that the relevant difference bits agree across every edge of a two-coloured subgraph.

The \(i,j\)-subgraph connects all \(x_t,y_t\). The \(i,h\)-subgraph connects all \(x_t\), and the \(j,h\)-subgraph connects all \(y_t\). Therefore fixed vectors
\[
\boldsymbol\lambda\in\mathcal B_i,
\qquad
\boldsymbol\mu\in\mathcal B_j
\]
exist such that, for every \(t\),
\[
\mathbf b(x_t)=\mathbf p_t\oplus\boldsymbol\lambda,
\qquad
\mathbf b(y_t)=\mathbf q_t\oplus\boldsymbol\mu.
\tag{3}
\]
The main path also gives \(\lambda_j=\mu_i\).

Translation by fixed vectors is a bijection of the product cube. Consequently,
\[
\left\{
\bigl(\mathbf b(x_t),\mathbf b(y_t)\bigr):
0\le t<m
\right\}
=
\mathcal B_i\times\mathcal B_j.
\]
The edges \(x_ty_t\) therefore realize every arc of \(Z_5\) between first-coordinate classes \(i\) and \(j\).

This conclusion holds for **every** choice of the free component bits.

## 3.4. Joining the ten pieces

Take one piece for every unordered pair of colours. To obtain a connected graph, order them as
\[
12,\ 23,\ 13,\ 14,\ 24,\ 25,\ 35,\ 34,\ 45,\ 15.
\]
Consecutive pairs share a colour. Identify their \(t=0\) core vertices of that colour, making no other identifications.

Each new piece meets the preceding union at exactly one vertex. Hence:

- planarity and bipartiteness are preserved;
- treewidth remains at most two;
- every two-coloured cycle would have to lie inside one piece, so \(\varphi\) remains acyclic.

The prototype vectors at the identified vertices are all zero, so they are compatible as well.

Each piece has
\[
2m+2\cdot3(m-1)=2042
\]
vertices. Nine identifications give
\[
10\cdot2042-9=20\,411
\]
vertices.

The argument in each piece remains valid after the identifications. Thus every \(\varphi\)-respecting homomorphism to \(Z_5\) realizes all arcs between every pair of its first-coordinate classes. Its arc image is exactly \(Z_5\).

By Proposition 1, the resulting graph is \(7\)-colourable. Alternatively, colour the pieces into \(Q\) one at a time; translations of \(Q\) allow their colours to be matched at each joining vertex.

Finally, suppose a coarsening of such an \(80\)-label colouring used a tournament \(T\). Since every arc of \(Z_5\) is represented by an arc of \(D\), the coarsening would induce a homomorphism
\[
Z_5\to T.
\]
Proposition 2 implies \(|V(T)|\ge80\). This proves the theorem. \(\square\)

# 4. What remains unresolved

The obstruction establishes a precise limitation:

> Starting from an arbitrary given acyclic five-colouring, optimizing all component-bit choices and then merging the resulting colour classes need not exploit planarity at all.

It does **not** rule out:

- choosing a different acyclic colouring;
- using a different encoding or target;
- splitting existing colour classes before recolouring;
- proving a smaller upper bound by a structural argument.

Indeed, the obstruction graph itself needs at most seven colours.

Thus the sharp subclass calculation and the encoding obstruction are complete, but the main problem remains undetermined here. Neither a planar example requiring more than \(18\) colours nor a general upper bound below \(80\) has been established.