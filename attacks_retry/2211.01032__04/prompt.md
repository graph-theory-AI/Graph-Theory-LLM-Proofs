Attack the following open graph-theory problem.

Catalog id: 2211.01032__04
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2211.01032__04/
Source paper: Random Embeddings of Graphs: The Expected Number of Faces in Most Graph… (arXiv:2211.01032)

=== Catalog page (statement + literature review) ===
Non-orientable embedding faces below orientable — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 9.6 asserts that the expected face count under a uniformly random non-orientable embedding never exceeds the expected face count under a uniformly random orientable embedding, for any graph G. No paper resolving or making substantial progress on this specific conjecture was found in the indexed literature. The conjecture is verified in the source paper only for toy cases (dipole, chains of triangles joined by cut edges), and the bound E[F^-] <= (1/2)E[F] + 1 is established for the dipole via Random Process A.

 Reviewer notes. No follow-up found after 4 web searches. The conjecture is recent (source paper first posted November 2022, published at SODA 2024, revised April 2025). Absence of follow-up is expected for a conjecture of this vintage in a specialized topological graph theory setting.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Let $F^{-}$ be the random variable for the average number of faces in a non-orientable random embedding of some graph $G$. Then $\mathbb{E}[F^{-}] \leq \mathbb{E}[F]$.

Context

The authors conjecture that the expected face count in a non-orientable random embedding is always at most that of the orientable random embedding, for any graph $G$. The inequality is verified for toy models (including the dipole and chains of triangles joined by cut edges), and an analysis of Random Process A gives the bound $\mathbb{E}[F^{-}] \leq \frac{1}{2}\mathbb{E}[F] + 1$ for the dipole.

Source paper

 Random Embeddings of Graphs: The Expected Number of Faces in Most Graphs is Logarithmic
 Jesse Campion Loth, Kevin Halasz, Tomáš Masařík, Bojan Mohar, Robert Šámal · 2025-04-09
 https://arxiv.org/abs/2211.01032

=== Source paper abstract / header ===
Abstract:A random 2-cell embedding of a connected graph $G$ in some orientable surface is obtained by choosing a random local rotation around each vertex. Under this setup, the number of faces or the genus of the corresponding 2-cell embedding becomes a random variable. Random embeddings of two particular graph classes, those of a bouquet of $n$ loops and those of $n$ parallel edges connecting two vertices, have been extensively studied and are well-understood. However, little is known about more general graphs. The results of this paper explain why Monte Carlo methods cannot work for approximating the minimum genus of graphs.
In his breakthrough work [Permutation-partition pairs, JCTB 1991], Stahl developed the foundation of "random topological graph theory". Most of his results have been unsurpassed until today. In our work, we analyze the expected number of faces of random embeddings (equivalently, the average genus) of a graph $G$. It was very recently shown that for any graph $G$, the expected number of faces is at most linear. We show that the actual expected number of faces $F(G)$ is almost always much smaller. In particular, we prove:
1) $\frac{1}{2}\ln n - 2 < \mathbb{E}[F(K_n)] \le 3.65 \ln n +o(1)$.
2) For random graphs $G(n,p)$ ($p=p(n)$), we have $\mathbb{E}[F(G(n,p))] \le \ln^2 n+\frac{1}{p}$.
3) For random models $B(n,\Delta)$ containing only graphs, whose maximum degree is at most $\Delta$, we obtain stronger bounds by showing that the expected number of faces is $\Theta(\log n)$.
 

 
 
 
 Comments:
 Accepted at the 35th ACM-SIAM Symposium on Discrete Algorithms (SODA 2024). The submission also contains sources and data of the computation described in the paper. 55 pages, 11 figures
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C10
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:2211.01032 [math.CO]
 

 
  
 (or 
 arXiv:2211.01032v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2211.01032
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Proceedings: ACM-SIAM Symposium on Discrete Algorithms, SODA 2024
 

 
 
 Related DOI:
 
 https://doi.org/10.1137/1.9781611977912.46

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Tomáš Masařík [view email] 
 [v1]
 Wed, 2 Nov 2022 10:58:31 UTC (500 KB)

 [v2]
 Thu, 28 Dec 2023 22:21:48 UTC (708 KB)

 [v3]
 Wed, 9 Apr 2025 18:37:40 UTC (1,123 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Random Embeddings of Graphs: The Expected Number of Faces in Most Graphs is Logarithmic, by Jesse Campion Loth and 4 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 math.CO

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2022-11
 

 Change to browse by:
 
 cs
 cs.DM
 math
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 export BibTeX citation
 Loading...

 
 
 BibTeX formatted citation

 ×
 

 
 loading...
 

 
 Data provided by: 
 
 

 

 Bookmark

 
 
 
 
 

 

 

 
 Bibliographic Tools
 
 Bibliographic and Citation Tools

 
 
 
 
 
 
 Bibliographic Explorer Toggle
 
 

 
 Bibliographic Explorer (What is the Explorer?)
 

 

 
 
 
 
 
 Connected Papers Toggle
 
 

 
 Connected Papers (What is Connected Papers?)
 

 

 
 
 
 
 Litmaps Toggle
 
 

 
 Litmaps (What is Litmaps?)
 

 

 
 
 
 
 
 scite.ai Toggle
 
 

 
 scite Smart Citations (What are Smart Citations?)
 

 

 

 

 

 

 

 

 
 Code, Data, Media
 
 Code, Data and Media Associated with this Article

 
 
 
 
 
 
 alphaXiv Toggle
 
 

 
 alphaXiv (What is alphaXiv?)
 

 

 
 
 
 
 
 Links to Code Toggle
 
 

 
 CatalyzeX Code Finder for Papers (What is CatalyzeX?)
 

 

 
 
 
 
 
 DagsHub Toggle
 
 

 
 DagsHub (What is DagsHub?)
 

 

 
 
 
 
 
 
 GotitPub Toggle
 
 

 
 Gotit.pub (What is GotitPub?)
 

 

 
 
 
 
 
 Huggingface Toggle
 
 

 
 Hugging Face (What is Huggingface?)
 

 

 
 
 
 
 
 ScienceCast Toggle
 
 

 
 ScienceCast (What is ScienceCast?)
 

 

 

 

 

 

 

 

 

 

 
 Demos
 
 Demos

 
 
 
 
 
 
 Replicate Toggle
 
 

 
 Replicate (What is Replicate?)
 

 

 
 
 
 
 
 Spaces Toggle
 
 

 
 Hugging Face Spaces (What is Spaces?)
 

 

 
 
 
 
 
 Spaces Toggle
 
 

 
 TXYZ.AI (What is TXYZ.AI?)
 

 

 

 

 

 

 

 
 Related Papers
 
 Recommenders and Search Tools

 
 
 
 
 
 
 Link to Influence Flower
 
 

 
 Influence Flower (What are Influence Flowers?)
 

 

 
 
 
 
 
 Core recommender toggle
 
 

 
 CORE Recommender (What is CORE?)
 

 

 

 
 
 Author

 Venue

 Institution

 Topic

 
 
 

 

 

 

 

 

 

 

 

 
 
 About arXivLabs
 
 
 
 
 arXivLabs: experimental projects with community collaborators

 arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

 Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

 Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.

 

 
 

 

 

 

 

 
 Which authors of this paper are endorsers? |
 Disable MathJax (What is MathJax?)

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-5.6-sol`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for every connected graph of cyclomatic number at most 3, as well as several broader sufficient classes, but the general rotation average remains unresolved.",
  "would_publish": false,
  "caveats": "This uses the standard uniformly weighted signed-rotation-system model; cyclomatic number at least 4 is not settled."
}
```

## 1. Statement of the partial result

All darts are regarded as labelled, as in the random-local-rotation model of the source paper. Let \(G\) be connected and put
\[
r=\beta(G)=|E(G)|-|V(G)|+1.
\]
Thus \(r\) is the dimension of the cycle space.

I prove the following.

### Theorem

Under the standard signed-rotation-system model:

1. The conjecture
   \[
   \mathbb E[F^-]\leq \mathbb E[F]
   \]
   holds for every connected graph with \(1\leq r\leq 3\).

2. More generally, it holds whenever
   \[
   \mathbb E[F]\geq 1+\frac r2.
   \]

3. It is closed under joining graphs by bridges. Consequently, it holds whenever every component left after deleting all bridges has cyclomatic number at most \(3\).

4. For any fixed nonzero signature class that has a balancing edge, its expected face count is at most the orientable expected face count.

There is also an exact linear-algebraic reformulation of the full conjecture, given below.

For \(r=0\), there is no nonorientable signature class, so the conditional nonorientable model is undefined.

---

## 2. Orientable versus signed rotation systems

Fix a spanning tree \(T\) of \(G\). A signed rotation system consists of:

- a cyclic order \(R_v\) of the darts incident with each vertex \(v\);
- an edge signature in \(\mathbb F_2^E\), where \(1\) means that the corresponding edge-band is twisted.

Switching at a vertex reverses its cyclic order and toggles the signatures of its non-loop incident edges. After switching, every signature class has a unique representative which is zero on \(T\). It is therefore represented by a vector
\[
d\in\mathbb F_2^r
\]
indexed by the cotree edges.

Because inversion is a bijection on the cyclic orders at each vertex, normalizing the tree-edge signs does not disturb the uniform distribution on rotations.

Let
\[
a_d=\mathbb E_R[F(R,d)].
\]
Then \(a_0=\mathbb E[F]\). If the nonorientable model is conditioned on having a nonzero signature class, let
\[
a_-=\frac{1}{2^r-1}\sum_{d\neq 0}a_d.
\]
If instead the source convention averages over all signed rotation systems, including the orientable class, let
\[
\bar a=\frac1{2^r}\sum_d a_d.
\]
These two formulations give equivalent inequalities, since
\[
\bar a-a_0
 =\frac{2^r-1}{2^r}(a_--a_0).
\]
Thus it is harmless for the truth of the conjecture whether \(F^-\) includes or excludes the single orientable signature class.

---

## 3. The overlap-matrix reformulation

Normalize the tree-edge signatures and contract all edges of \(T\). This does not change the number of boundary components of the ribbon surface. The result is a one-vertex ribbon graph with \(r\) loop-bands.

For an orientable rotation \(R\), define the \(r\times r\) matrix
\[
A=A(R,T)
\]
over \(\mathbb F_2\) by

- \(A_{ii}=0\);
- for \(i\neq j\), \(A_{ij}=1\) exactly when the two pairs of endpoints corresponding to cotree edges \(i,j\) alternate around the contracted vertex.

Thus \(A\) is symmetric and alternating. If the normalized signature is \(d\), twisting the corresponding bands changes only the diagonal, giving
\[
A_d=A+\operatorname{Diag}(d).
\]

### Lemma 3.1
For every rotation \(R\) and normalized signature \(d\),
\[
F(R,d)=1+\nu\!\left(A(R,T)+\operatorname{Diag}(d)\right),
\tag{3.1}
\]
where \(\nu\) denotes nullity over \(\mathbb F_2\).

#### Proof

Let \(N\) be the compact ribbon surface before its boundary components are capped. It deformation-retracts onto \(G\), so
\[
\dim H_1(N;\mathbb F_2)=r.
\]
The core curves of the \(r\) cotree bands form a basis. Their mod-\(2\) intersection matrix is \(A+\operatorname{Diag}(d)\): distinct curves intersect according to endpoint alternation, while a core curve has self-intersection \(1\) exactly when its band is twisted.

For every connected compact surface with \(b\) boundary components, the radical of its mod-\(2\) intersection form has dimension \(b-1\). This follows directly from the classification of compact surfaces: the boundary classes span the radical with their one relation that their sum is zero, while the form on the handle or crosscap part is nonsingular.

Since the boundary components of \(N\) are precisely the faces,
\[
\nu(A+\operatorname{Diag}(d))=F(R,d)-1.
\]
This proves (3.1). ∎

Consequently, the original conjecture is equivalent to
\[
\mathbb E_R\nu(A_R)
\ \geq\
\mathbb E_R\frac1{2^r-1}
       \sum_{0\neq d\in\mathbb F_2^r}
       \nu\!\left(A_R+\operatorname{Diag}(d)\right).
\tag{3.2}
\]

---

## 4. A universal diagonal-averaging bound

### Lemma 4.1
For every \(r\times r\) matrix \(A\) over \(\mathbb F_2\),
\[
\frac1{2^r}\sum_{d\in\mathbb F_2^r}
\nu\!\left(A+\operatorname{Diag}(d)\right)
\leq \frac r2.
\tag{4.1}
\]

#### Proof

Pair \(d\) with \(d+\mathbf 1\), where \(\mathbf 1=(1,\ldots,1)\). Put
\[
M=A+\operatorname{Diag}(d).
\]
The paired matrix is \(M+I_r\). Since
\[
\operatorname{rank}(M)+\operatorname{rank}(M+I_r)
   \geq \operatorname{rank}(I_r)=r,
\]
we have
\[
\nu(M)+\nu(M+I_r)\leq r.
\]
Averaging over the \(2^{r-1}\) pairs proves (4.1). ∎

By (3.1), for every fixed rotation,
\[
\frac1{2^r}\sum_d F(R,d)\leq 1+\frac r2.
\tag{4.2}
\]
For the conditional nonorientable average, one obtains the slightly sharper bound
\[
\frac1{2^r-1}\sum_{d\neq0}\nu(A+\operatorname{Diag}(d))
\leq
\frac{2^{r-1}r-\nu(A)}{2^r-1}.
\tag{4.3}
\]

Averaging (4.2) over rotations proves:

### Corollary 4.2
If
\[
\mathbb E[F]\geq 1+\frac r2,
\]
then the conjecture holds.

Equivalently, since an orientable embedding satisfies
\[
F=r+1-2g,
\]
the conjecture holds whenever the average orientable genus is at most \(r/4\).

---

## 5. Proof for cyclomatic number at most three

### 5.1. The case \(r=1\)

Every orientable embedding has genus zero, hence
\[
F=r+1=2.
\]
Thus \(\mathbb E[F]=2>3/2\), and Corollary 4.2 applies. In fact every nonorientable signature gives one face.

---

### 5.2. The case \(r=2\)

It suffices to prove
\[
\mathbb E[F]\geq 2.
\tag{5.1}
\]

Deleting pendant edges does not change the face count. Moreover, deleting a specified dart from a uniformly random cyclic order leaves a uniformly random cyclic order on the remaining darts. Suppressing degree-two vertices likewise preserves the ribbon surface and introduces no rotation choices.

After these operations, a connected graph of cyclomatic number \(2\) has one of three kernels. Indeed,
\[
\sum_v(\deg(v)-2)=2r-2=2.
\]
Hence the kernel is one of:

1. a bouquet of two loops;
2. three parallel edges between two degree-three vertices;
3. two looped vertices joined by a bridge.

For the two-loop bouquet there are \(6\) cyclic orders. Four are noninterlacing and have \(3\) faces, while two are interlacing and have \(1\) face. Thus
\[
\mathbb E[F]=\frac{4\cdot3+2\cdot1}{6}=\frac73.
\]

For the three-edge dipole, there are \(2\cdot2=4\) rotation systems. Two have three faces and two have one face, giving
\[
\mathbb E[F]=2.
\]

For the dumbbell kernel, the bridge joins two annular ribbon surfaces and every orientable rotation has
\[
F=2+2-1=3.
\]

Thus (5.1) always holds. Since \(1+r/2=2\), Corollary 4.2 proves the conjecture for \(r=2\).

---

### 5.3. The case \(r=3\)

Here one can prove the required inequality for every fixed orientable rotation before averaging over rotations.

Every alternating \(3\times3\) matrix is the adjacency matrix over \(\mathbb F_2\) of one of the following four graphs on three labelled coordinates, up to coordinate permutation. Direct enumeration of the seven nonzero diagonal vectors gives:

\[
\begin{array}{c|c|c}
\text{off-diagonal support of }A
&
\nu(A)
&
\displaystyle
\frac17\sum_{d\neq0}\nu(A+\operatorname{Diag}(d))
\\ \hline
\varnothing &3&9/7\\
\text{one edge}&1&5/7\\
\text{two-edge path}&1&2/7\\
\text{triangle}&1&5/7
\end{array}
\]

Every entry in the third column is at most the corresponding entry in the second column. Therefore, for every rotation \(R\),
\[
\frac17\sum_{d\neq0}F(R,d)\leq F(R,0).
\]
Averaging over \(R\) proves the conjecture for all connected graphs with \(r=3\).

This completes the proof for \(r\leq3\).

---

## 6. Closure under bridges

Suppose that a bridge joins two connected graphs \(G_1,G_2\). For every signed rotation system,
\[
F(G)=F(G_1)+F(G_2)-1.
\tag{6.1}
\]
Topologically, the bridge-band joins one boundary component from each of two initially disjoint ribbon surfaces. Its twist does not affect the boundary count.

Deleting the bridge dart from a uniform cyclic order leaves a uniform cyclic order, so (6.1) also holds after taking expectations. Hence
\[
\mathbb E_{\rm all\ signs}[F(G)]
=
\mathbb E_{\rm all\ signs}[F(G_1)]
+\mathbb E_{\rm all\ signs}[F(G_2)]-1,
\]
and the analogous identity holds in the orientable model.

It follows that the conjecture is preserved under joining graphs by bridges. In particular, it holds whenever every component obtained after deleting all bridges has cyclomatic number at most \(3\).

---

## 7. Signature classes with a balancing edge

A nonzero signature class has a balancing edge \(e\) if it is switching-equivalent to the signature in which \(e\) is the unique negative edge. Equivalently, deleting \(e\) makes the signed graph balanced.

### Lemma 7.1
If \(A\) is alternating over \(\mathbb F_2\), then
\[
\ker(A+E_{ii})\subseteq\ker(A),
\]
and hence
\[
\nu(A+E_{ii})\leq\nu(A).
\tag{7.1}
\]

#### Proof

Let \(x\in\ker(A+E_{ii})\). Since \(A\) is alternating,
\[
0=x^{\mathsf T}(A+E_{ii})x=x_i.
\]
Thus \(E_{ii}x=0\), and consequently \(Ax=0\). ∎

If a signature class has balancing edge \(e\), choose a spanning tree avoiding \(e\). In the normalized signature, the diagonal perturbation is exactly one \(E_{ii}\). Equation (7.1), together with (3.1), gives
\[
F(R,\text{that signature})\leq F(R,0)
\]
after the appropriate vertex switch. Since vertex switching acts measure-preservingly on random rotations, this yields
\[
\mathbb E_R[F(R,\text{that class})]\leq\mathbb E[F].
\]

Thus every balancing-edge class satisfies the conjectured comparison individually.

---

## 8. A uniform-overlap sufficient condition

There is another useful algebraic case.

### Proposition 8.1
Suppose that, for some spanning tree \(T\), the random overlap matrix \(A(R,T)\) is uniform over all alternating \(r\times r\) matrices over \(\mathbb F_2\). Then every nonzero signature class has strictly smaller expected nullity, and hence strictly smaller expected face count, than the orientable class.

#### Proof

Let \(V=\mathbb F_2^r\), and fix a nonzero linear functional \(q\). A uniform symmetric bilinear form \(B\) satisfying
\[
B(x,x)=q(x)
\]
has the same distribution as \(A+\operatorname{Diag}(d)\) for a fixed nonzero \(d\) and uniform alternating \(A\).

Choose \(u\) with \(q(u)=1\), and put \(H=\ker q\). Then \(B\) is determined by:

- a uniform alternating form \(C=B|_H\);
- an independent uniform functional \(\ell=B(u,\cdot)|_H\);
- \(B(u,u)=1\).

Let \(K=\operatorname{rad}C\) and \(k=\dim K\). Since every radical vector of \(B\) lies in \(H\),
\[
\operatorname{rad}B=K\cap\ker\ell.
\]
Thus
\[
\mathbb E[\nu(B)\mid C]
   =k-1+2^{-k}.
\tag{8.1}
\]

For a uniform alternating form on \(V\), the same decomposition has \(B(u,u)=0\). If \(\ell\) annihilates \(K\), which occurs with probability \(2^{-k}\), the radical has dimension \(k+1\); otherwise it has dimension \(k-1\). Therefore
\[
\mathbb E[\nu(A)\mid C]
   =k-1+2^{1-k}.
\tag{8.2}
\]
The difference between (8.2) and (8.1) is \(2^{-k}>0\). ∎

### Example: \(K_4\)

For \(K_4\), take the star at vertex \(4\) as spanning tree and let the cotree edges be \(12,13,23\). Choose one planar rotation as reference, and let \(x_i\in\mathbb F_2\) indicate whether the rotation at vertex \(i\) has been reversed. A direct contraction calculation gives
\[
A_{12,13}=x_1+x_4,\qquad
A_{12,23}=x_2+x_4,\qquad
A_{13,23}=x_3+x_4.
\]
Hence \(A\) is uniform over all eight alternating \(3\times3\) matrices.

It follows that
\[
\mathbb E[F(K_4)]=\frac94.
\]
For each fixed nonzero signature class, Proposition 8.1 gives expected nullity \(5/8\), hence
\[
\mathbb E[F^-(K_4)\mid\text{nonorientable}]=\frac{13}{8}.
\]
If the model averages over all eight signature classes, including the orientable one, then
\[
\mathbb E[F^-_{\rm all}(K_4)]
=\frac18\left(\frac94+7\cdot\frac{13}{8}\right)
=\frac{109}{64}.
\]

---

## 9. Exact enumeration protocol

The preceding small examples can be checked without any topological simplification.

Let \(D\) be the dart set, \(\alpha\) the edge-reversal involution, \(\sigma\) the product of the local rotations, and \(t_e\) the edge-twist bits. On signed darts \(D\times\mathbb F_2\), define
\[
s'=s+t_{e(h)}
\]
and
\[
\Phi(h,s)=
\begin{cases}
\bigl(\sigma(\alpha h),s'\bigr),&s'=0,\\[2mm]
\bigl(\sigma^{-1}(\alpha h),s'\bigr),&s'=1.
\end{cases}
\tag{9.1}
\]
Every boundary component gives two oppositely directed cycles of \(\Phi\), so
\[
F=\frac12\,c(\Phi).
\]

Enumerating the \(\prod_v(\deg(v)-1)!\) rotations and the \(2^r\) normalized signatures gives the following exact values:

\[
\begin{array}{c|c|c|c|c}
G&r&\mathbb E[F]
&\mathbb E[F^-\mid d\neq0]
&\mathbb E[F^-_{\rm all}]
\\ \hline
\text{one-loop bouquet}&1&2&1&3/2\\
\text{two-loop bouquet}&2&7/3&14/9&7/4\\
\text{three-edge dipole}&2&2&3/2&13/8\\
K_4&3&9/4&13/8&109/64
\end{array}
\]

These are exact rational enumerations, not Monte Carlo estimates.

---

## 10. Why this does not prove the full conjecture

The essential remaining problem is inequality (3.2) for overlap matrices arising from random rotations when \(r\geq4\).

A comparison for each fixed rotation is false. For example, let
\[
A=
\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&0&1\\
0&0&1&0
\end{pmatrix}
=H\oplus H.
\]
Then \(\nu(A)=0\). For uniform nonzero \(d\in\mathbb F_2^4\), each \(2\times2\) block acquires nullity one exactly when both corresponding diagonal bits are \(1\). Therefore
\[
\frac1{15}\sum_{d\neq0}\nu(A+\operatorname{Diag}(d))
=\frac8{15}>0.
\]
This matrix is realizable by a fixed rotation of the four-loop bouquet, for instance by the cyclic endpoint order
\[
1,2,1,2,3,4,3,4.
\]
Thus averaging over rotations is genuinely indispensable.

The arguments above do not control how frequently such low-nullity overlap matrices occur in the random-rotation distribution. That distributional question is the unresolved part of the conjecture.
