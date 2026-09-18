---
id: finding_k_edge_outerplanar_graph_embeddings
leg: attacks_opg
claimed_verdict: proved
review_verdict: ALREADY_KNOWN
confidence: high
interpretation_ok: true
references_ok: true
computation_run: true
one_line: The SPQR dynamic program is, as far as I could check, correct — every recurrence (S, P, Q, R, the two-arm P-node scheduling DP, the block-cut gluing lemma) reproduces brute force on thousands of small instances — but the theorem was already published two months earlier as arXiv:2607.08110 (H. Yu, 9 July 2026), which resolves Bentz's question by a different route.
---

## Interpretation

The prompt asks Bentz's question as posed on OpenProblemGarden: Bienstock–Monma showed that a
$k$-outerplanar embedding with minimum $k$ is computable in polynomial time; does the same hold
for **edge**-outerplanarity, where each round deletes all edges lying on the current outer face?

The writeup formalizes exactly this. Its Theorem reads: "Given a finite planar graph $G$, one can
compute, in polynomial time, a plane embedding of $G$ minimizing the number of rounds of
simultaneous deletion of all edges incident with the outer face." That is the intended reading:

* the minimization ranges over **both** the combinatorial embedding and the choice of outer face
  (as it must — "an embedding with at most $k$ layers of edges");
* the peeling process is the literal one from the OPG discussion (delete all outer-face edges,
  repeat, until no edge remains);
* the output is an embedding, not merely the value $k$, matching "finding … embeddings" in the title.

No strawman or literal-reading gaming: the writeup answers the question in the affirmative, in the
strong form (a constructive polynomial algorithm), and does not weaken the hypothesis to, e.g.,
fixed $k$ or fixed embedding. A reasonable author of the original problem would consider the
question resolved by this statement. **interpretation_ok: true.**

One convention is chosen and stated: for an edgeless graph the optimum is declared $0$ (or $1$ if
the parameter must be positive). Harmless.

The one interpretive mismatch is not mathematical but bibliographic: the verdict block sets
`would_publish: true`, whereas the theorem had already appeared on arXiv on 9 July 2026 (see
**Reference check**). The writeup is honest about this — its own caveat says "novelty and current
literature status have not been independently checked" — but the claim as scored is a
re-derivation of a known theorem.

## Step-by-step findings

Every numbered item below was re-derived by hand; the ones marked "(code)" were additionally
verified by brute force (see **Computational check**).

| # | step | label | note |
|---|------|-------|------|
| 1 | §1 Theorem + conventions ($0$ for edgeless; output is an embedding) | VALID | Statement is the intended one; conventions stated explicitly. |
| 2 | §2 Lemma 1: $\mathrm{layer}(e)=1+\min\{d(f_e),d(g_e)\}$ | VALID (code) | Proof is one terse paragraph ("follows inductively"). The missing sentence is that after a round the faces absorbed into the outer region are exactly those joined to it by a deleted edge, so the absorbed set is the dual BFS ball. Verified on 544 (embedding, outer face) pairs over 40 random planar graphs by an independent region-merging simulation; also confirmed by the literature (Lemma 3.2 of arXiv:2607.08110 is the same identity). |
| 3 | §2 eq. (2): $K(G,r)=\max_e(1+\min\{d(f_e),d(g_e)\})$ | VALID | Immediate from step 2. The remark that this is *not* the eccentricity of $r$ in the dual, with $K_4$ as witness (eccentricity 1, peeling 2), is correct — I recomputed $K_4=2$. |
| 4 | §2 Deletion monotonicity | VALID | Deleting edges merges faces, so dual distances do not increase; used only in Lemma 3's lower bound, where it is applied legitimately (the outer face is inherited, and it stays a face because an edge of $B$ lies on it). |
| 5 | §3 weighted objective $\Psi(B,w)=\max\{K(B,r),\max_v(w(v)+a_B(v))\}$; remark that $w\equiv0$ adds nothing | VALID | For nonisolated $v$ an edge bounding a nearest incident face has layer $a_B(v)+1>a_B(v)$, so the vertex terms are dominated; $B$ biconnected has no isolated vertex. |
| 6 | §4 rooted pertinent component, $D_H=(\widehat H)^*-\rho^*$ | VALID | $D_H$ is connected because $\rho$ is not a loop; $A\neq B$ because $\widehat H$ is biconnected. |
| 7 | §4.1 Lemma 2: $\ell(H)=\mathrm{dist}_{D_H}(A,B)$ is embedding-invariant, $1\le\ell\le|E(H)|$ | VALID, proof GAP (code) | The S/P/R induction is correct but silently uses "a dual path through a child may be replaced by an edge of length $\ell(H_i)$", which needs the (true) separator remark that such a path enters and leaves at the child's two boundary faces. A cleaner embedding-free proof exists and I verified it: shortest dual cycles through $\rho^*$ are minimum bonds containing $\rho$, so $\ell(H)$ is exactly the minimum $s$–$t$ edge cut of $H$. Verified on 412 (biconnected graph, reference edge) pairs: the value was constant over all genus-0 rotation systems and equal to the max-flow value every time. |
| 8 | §4.2 profile $F_H(d)$, eq. (6) $\delta(z)=\min\{\mathrm{dist}(A,z),\,d+\mathrm{dist}(B,z)\}$ | VALID (code) | Correct because $D_H$ meets the rest of the dual only in $\{A,B\}$. |
| 9 | §4.2 eq. (7): contribution $=\min\{a,b\}+F_H(|a-b|)$, using that reflection swaps $A,B$ | VALID (code) | The cost is a max of terms "constant $+\delta$", so it shifts by $\min\{a,b\}$; and reflecting a rotation system maps faces by $h\mapsto\alpha(h)$, which does exchange the two $\rho$-faces. 6701 (component, $\rho$, $a$, $b$) cases: identity held exactly, and $F_H(0,d)=F_H(d,0)$ in every case. |
| 10 | §4.2 eq. (8): real-edge leaf has $\ell=1$, $F(0)=F(1)=1$ | VALID | Single dual edge with labels $0,d$; $1+\min\{0,d\}=1$. This is the Q-node case, so all four node types are covered. |
| 11 | §5 eqs. (9)–(10) and the side condition $|\delta(x_i)-\delta(y_i)|\le\ell_i$ | VALID (code) | $\delta$ is 1-Lipschitz for $\mathrm{dist}_W$, and $\mathrm{dist}_W(x_i,y_i)\le\ell_i$. My R-node harness asserted this inequality on every evaluation; it never fired. |
| 12 | §5 "child optimization is independent" | VALID | Nothing outside a child sees its embedding except through the invariant $\ell_i$; the objective is a max of per-child terms, so per-child minimization is exact. No greedy exchange is assumed here. |
| 13 | §5 eq. (11): vertex weights localize to skeleton faces | VALID (code) | A face inside child $i$ incident with $v$ has $\delta\ge\min\{\delta(x_i),\delta(y_i)\}$, and both $x_i,y_i$ are incident with $v$. Verified indirectly: the R- and S-node composition tests carried skeleton-vertex weights and matched the true profile, which minimizes over *all* faces at $v$. |
| 14 | §5 eq. (12): $C_\Sigma(a,b)$ | VALID | Partition of internal vertices into "internal to one child" / "skeleton, non-pole" is correct. |
| 15 | §5.1 eq. (13): $F_H(d)=\min\{C_\Sigma(0,d),C_\Sigma(d,0)\}$ at an R-node | VALID (code) | The mirror skeleton has the same dual with $A,B$ exchanged, so swapping the labels is exactly the reflection. 830 (R-composition, $d$) cases over $K_4$ and the 3-prism as skeletons: the writeup's rule on one fixed skeleton embedding agreed with the true brute-force profile every time, and also with the minimum over both skeleton embeddings. |
| 16 | §5.2 eq. (14): $\ell=\min_i\ell_i$, $F_H(d)=\max\{\max_iF_i(d),\max_v w(v)\}$ at an S-node | VALID (code) | All children share the same two faces; every internal cycle vertex is incident with both, so its term is $w(v)+\min\{0,d\}=w(v)$. 65 (S-composition, $d$) cases, no mismatch. |
| 17 | §6 eqs. (15)–(17): $\Lambda=\sum\ell_i$, meeting point $h=(\Lambda+d)/2$, central child, condition $\lvert\alpha-\beta\rvert\le\ell_j$ | VALID | $h\in[\Lambda/2,\Lambda]\subseteq[0,\Lambda]$ for $0\le d\le\Lambda$, so a central child always exists. I re-derived $\lvert\alpha-\beta\rvert\le\ell_j\iff h-\ell_j\le X\le h$, i.e. exactly "$h$ lies in child $j$". The labels $\alpha=X$, $\beta=d+Y$ are the correct branch of $\min$ on each side. |
| 18 | §6.1 exchange argument: each arm sorted by nonincreasing $q_i=p_i-\ell_i$ | VALID (code) | Re-derived: with $q_i\ge q_j$, $\max\{A+\ell_i+q_i,\;A+\ell_i+\ell_j+q_j\}\le A+\ell_i+\ell_j+q_i$, which is one of the two costs of the swapped order. Arm length, and hence the central child's contribution, is unchanged. This is the only exchange property used and it is genuinely proved, not assumed. |
| 19 | §6.2 eqs. (19)–(21): the two-bin assignment DP | VALID (code) | State is the left-arm length $x$, which is $O(\Lambda)=O(|E(H)|)$ — genuinely polynomial, *not* exponential in a hidden parameter, because the $\ell_i$ are unary-bounded by edge counts. The right-arm accounting $d+(S-x)+p_i$ is correct: the right arm is emitted in reverse, so the length accumulated so far is exactly the suffix length after that child. 173 (real P-composition, $d$) cases matched both brute force over all $r!$ orders and the true brute-force profile; 4000 random and 4000 monotone/Lipschitz synthetic profile instances with up to 5 children matched brute force over orders with zero exceptions. |
| 20 | §6.3 completeness of the P-recurrence (junction case, $d=\Lambda$, one child) | VALID | Both directions re-checked; $r\ge2$ always at a genuine P-node. |
| 21 | §6.4 eq. (22): $O(r^2\Lambda^2)$ per P-node | VALID | $O(\Lambda)$ states $\times$ $r$ stages $\times$ $r$ choices of $j$ $\times$ $(\Lambda+1)$ values of $d$. Summing over P-nodes gives $O(N^4)$ since $\sum r_i=O(N)$. |
| 22 | §7 eq. (23): $\mathrm{Opt}(B,w;e)=\max\{1,F_H(1),w(s),w(t)\}$ | VALID (code) | The far $\rho$-face is at distance $\min\{1,\ell(H)\}=1$ since $\ell\ge1$; both ends of $e$ are on the outer face so $a_B=0$ there. Verified against brute force for every edge of 40 random blocks under 3 random weightings each. |
| 23 | §7 eqs. (24)–(25): minimize over root edges; constrained version at a vertex $c$ | VALID (code) | Every embedding has some edge on the outer face; a vertex on the outer face of a biconnected graph has an incident edge there. 120 unconstrained and $40\times3\times n$ vertex-constrained comparisons, all exact. |
| 24 | §8.1 Lemma 3, upper bound | VALID | Gluing a branch inside a face $f_v$ joins the two duals at the single vertex $f_v$, so branch layers shift by exactly $d(f_v)=a_B(v)$ and distances inside $B$ are unchanged. |
| 25 | §8.1 Lemma 3, lower bound | VALID, proof GAP | The key sentence — "Because an edge of $B$ is on the outer face, the branch does not enclose $B$; in its induced standalone embedding, $v$ is therefore incident with the outer face" — is correct but compressed. The repair: $B-v$ is connected and disjoint from the branch, so it lies in one face $F'$ of the branch; the graph's outer face is incident with an edge of $B$, hence contained in $F'$, hence $F'$ is the branch's outer face, and $v$ is on its boundary. The "delete the other branches" device handles nesting correctly. |
| 26 | §8.2 block-cut-tree DP; bridge blocks eq. (28); enumeration of root blocks | VALID (code) | Each branch $H_{v,i}$ contains exactly one block at $v$, so "$v$ on the outer face of the branch" $\iff$ "outer-face incidence in that block", as claimed. 40 random graphs with cut vertices plus 11 hand-built stress cases (nested $K_4$s, pendant paths, a tree, $K_5-e$ with a pendant, a chain of blocks) all matched brute force. |
| 27 | §8.2 disconnected graphs: answer is the max over components | VALID | Side-by-side placement gives $\le$; restriction plus deletion monotonicity gives $\ge$. (Not machine-checked: my brute-force enumerator uses Euler's formula and so is restricted to connected graphs. The argument is elementary.) |
| 28 | §9 overall bound $O(N^8)$ | VALID | Coarse but correct: $O(N^5)$ per rooted SPQR computation, $\times N$ root edges $\times N$ blocks $\times N$ root blocks. The per-node accounting is asserted rather than itemized, but each assertion checks out ($O(N^2\log N)$ per R-node over all $d$, entrywise maxima at S-nodes, eq. (22) at P-nodes). All values are $O(N)$-bounded, so arithmetic is on $O(\log N)$-bit integers as claimed. |
| 29 | §9 reconstruction of the embedding from stored minimizers | GAP | Asserted in a list, not proved. Routine for a DP of this shape (every choice made is local and realizable), but no argument is given that the retained choices assemble into a consistent rotation system. Not load-bearing for the complexity claim. |
| 30 | §9 multigraphs and loops | GAP | Parallel edges are genuinely covered (P-nodes; I checked bundles of $1..6$ parallel edges brute-force: $1,1,2,2,3,3=\lceil k/2\rceil$, and the P-node DP reproduces $2$ for the triple edge by hand). Loops are dispatched in a single sentence ("an elementary one-edge block, with the same value formula as (28)"), with no justification and no discussion of the non-standard block-cut conventions loops induce. The competing published proof explicitly restricts to loopless graphs. The claim is believable but unargued. |
| 31 | verdict block: `would_publish: true` | ERROR (bibliographic, not mathematical) | The theorem was published on arXiv two months before this writeup was generated. The writeup's own caveat acknowledges that literature status was not checked. |

No step was found to be mathematically wrong. The specific failure modes I was asked to hunt for
are all absent: the DP state is a single integer bounded by $|E(H)|$ (step 19), the recurrence
covers S, P, Q and R nodes including the R-node reflection (steps 10, 15, 16, 19), the two-bin
scheme's only exchange property is proved rather than assumed (step 18), and the running-time
accounting includes the product over $j$, $d$, root edges and root blocks (steps 21, 28).

## Reference check

* **SPQR decomposition theorem and its completeness for planar embeddings** — the writeup's only
  external structural dependency. Confirmed: the SPQR tree of Di Battista and Tamassia represents
  all planar embeddings of a biconnected planar graph; S- and Q-node skeletons have a unique
  embedding, an R-node skeleton (triconnected) has exactly two (mirror images), and a P-node
  skeleton (a bundle of $\ge3$ parallel edges) has one embedding per permutation of its edges; all
  embeddings are obtained by permuting P-node virtual edges and flipping R-node skeletons. This is
  exactly what §7 invokes. Note that "flipping a child component" is not an extra degree of
  freedom on top of this — it is generated by the deeper P-permutations and R-reflections — and the
  writeup's use of $F_H$ as a reflection-symmetric profile is consistent with that; I verified
  this directly by comparing composed profiles against brute force over *all* rotation systems
  (checks 5, 6, 7), which is the strongest available check of the completeness claim.
* **B. Bollobás / Baker / Bienstock–Monma / Bentz** — the writeup explicitly uses *none* of these
  ("No result about optimizing outerplanarity is used"), so there is nothing to misquote.
  Bienstock–Monma, *On the complexity of embedding planar graphs to minimize certain distance
  measures*, Algorithmica 5 (1990) 93–109 and Bentz, *Disjoint paths in sparse graphs*, Discrete
  Appl. Math. 157 (2009) 3558–3568 both exist as cited in the prompt; the Springer page for the
  former is behind an authentication redirect and I could not read its statement, but nothing in
  the writeup depends on it.
* **Priority — the decisive finding.** The theorem is already in the literature:
  **Hantao Yu (Columbia University), "Minimum Edge-Outerplanar Embeddings are Polynomial-Time
  Computable", arXiv:2607.08110, submitted 9 July 2026.** Abstract: "the minimum
  edge-outerplanarity of a planar graph can be computed in polynomial time, resolving an open
  problem of Bentz (2009)"; the paper also notes "The proof was initially produced by GPT~5.5 Pro
  and then verified and polished manually." Its route is *different* from the writeup's: it builds
  an auxiliary graph $H$ by subdividing each edge $e$ of $G$ with a vertex $s_e$ and attaching a
  marker triangle to $s_e$ through a bridge ($|V(H)|=|V(G)|+4|E(G)|$), and shows
  $\mathrm{OPT}_{\text{depth}}(H)=\mathrm{OPT}_{\text{edge}}(G)$ (its Lemmas 5.1 and 6.2), thereby
  reducing to the known polynomial-time minimum-face-depth embedding problem. Its Lemma 3.2 is
  *verbatim the writeup's Lemma 1*: $\lambda_\Gamma(e)=1+\min_{f\in F_\Gamma(e)}d_\Gamma(f)$. It
  restricts to loopless planar multigraphs and handles disconnected graphs componentwise
  (its Lemma 7.1), matching the writeup's §8 claim. The catalog page's "open, medium confidence"
  status is dated 2026-05-08, two months before that paper appeared, which explains the stale
  status.

So: `references_ok: true` (nothing is misquoted; the single invoked theorem is real and correctly
stated), but the *result* is not new.

## Computational check

Scripts: `verification_astra/scripts/finding_k_edge_outerplanar_graph_embeddings/`
(`run_all.sh` reproduces everything; `python3`, networkx 3.6.1). `pl.py` enumerates *all*
rotation systems of a (multi)graph, keeps the genus-0 ones via $V-E+F=2$, builds faces as orbits
of $h\mapsto\sigma(\alpha(h))$, and computes dual distances, layers and peeling rounds. `prof.py`
computes the writeup's profiles $F_H(d)$ by brute force over all embeddings. The strategy is to
brute-force every ingredient the writeup would compute recursively, and compare the writeup's
recurrences against ground truth at every level.

| check | what it tests | scale | result |
|---|---|---|---|
| `check1_lemma1.py` | Lemma 1 vs. an independent region-merging peeling simulation | 544 (embedding, outer face) pairs, 40 graphs, plus a bridge/multigraph case | **0 mismatches**. Sanity: $K_4\to2$, $K_5-e\to3$, triangle $\to1$ |
| `check2_ell.py` | Lemma 2: $\ell(H)$ constant over embeddings and $=$ max-flow $s$–$t$ in $H$ | 412 (block, reference edge) pairs | **0 mismatches**; $\ell$ was single-valued in every case |
| `check3_profile.py` | eq. (7): $\min_\varepsilon\mathrm{cost}(a,b)=\min\{a,b\}+F_H(\lvert a-b\rvert)$; and $F(0,d)=F(d,0)$ | 6701 $(H,\rho,a,b)$ cases with random vertex weights | **0 mismatches, 0 reflection asymmetries** |
| `check4_toplevel.py` | eqs. (23)–(25) vs. brute-force $\min\Psi(B,w)$ | 40 blocks $\times$ 3 weightings; unconstrained, per-edge and per-vertex-constrained | **0 mismatches** in all three modes |
| `check5_pnode.py` | P-node: two-bin DP vs. brute force over all $r!$ orders, **and** vs. the true profile of the composed graph | 173 (composition, $d$) cases | **0 mismatches** in both comparisons |
| `check5b_pnode_random.py` | the two-bin DP as a pure scheduling claim, on synthetic profiles | 4000 arbitrary + 4000 monotone/1-Lipschitz instances, up to 5 children | **0 mismatches** — the DP is correct even for profiles no graph realizes, i.e. the exchange property is genuinely unconditional |
| `check6_snode.py` | eq. (14) vs. true profile of a series composition | 65 (composition, $d$) cases with internal weights | **0 mismatches** |
| `check7_rnode.py` | eqs. (12)–(13) with $K_4$ and 3-prism skeletons vs. true profile; also asserts $\lvert\delta(x_i)-\delta(y_i)\rvert\le\ell_i$ | 830 (composition, $d$) cases | **0 mismatches**, Lipschitz assertion never fired, and the writeup's single-embedding rule $\min\{C(0,d),C(d,0)\}$ always equalled the minimum over both skeleton embeddings |
| `check8_cutvertex.py` | Lemma 3 + §8.2 block-cut DP vs. brute force on the whole graph | 40 random connected planar graphs with cut vertices | **0 mismatches** |
| `check9_hard.py` | hand-built stress cases: nested $K_4$s, pendant paths at a depth-1 vertex, wheel + pendant, tree, $K_5-e$ + pendant, chain of blocks | 11 instances, up to 7680 rotation systems each | **0 mismatches** |
| `check10_endtoend.py` | full pipeline (eqs. (23)–(25) inside the block-cut DP) vs. brute force; plus parallel bundles | 35 graphs; bundles of $1..6$ parallel edges | **0 mismatches**; bundles give $1,1,2,2,3,3=\lceil k/2\rceil$, which is what the P-node DP predicts (I also did $k=3$ by hand: $F_H(1)=2$) |
| `check11_sweep.py` | larger sweep, different seed, 4–9 vertices | 60 graphs, optima $\{1:26,\;2:30,\;3:4\}$ | **0 mismatches** |

Every recurrence in the writeup was compared against ground truth obtained by enumerating *all*
genus-0 rotation systems, and none of them failed. In particular there is no counterexample to the
two-bin scheme, none to $\ell$-invariance, and none to the gluing lemma. The one part of the
algorithm not exercised is the SPQR *construction* itself (I substituted brute-force profiles at
each level instead of building SPQR trees); since each composition rule was verified exactly and
the induction is over the tree, this is a complete check modulo the cited SPQR theorem.

## Caveats

1. **Priority.** The result is not new: arXiv:2607.08110 (9 July 2026) proves the same theorem,
   by a different and considerably shorter argument (a gadget reduction to minimum face-depth).
   The writeup's algorithm is a genuinely independent, self-contained proof — and, unlike the
   published one, it does not invoke Bienstock–Monma as a black box — but it cannot be said to
   resolve an open problem as of 2026-09-16. The writeup itself flags this risk in its caveats.
2. **Loops.** Dismissed in one sentence in §9. The published proof explicitly restricts to
   loopless graphs. A loop is not a block under the usual conventions, and no argument is given
   that the "one-edge block" treatment is sound; I believe it is (a loop is always best drawn with
   a side on the current outer region), but it is unargued.
3. **Reconstruction.** §9 lists the data to retain but does not argue that the retained minimizers
   assemble into a consistent rotation system. Routine, but not proved; the theorem statement in
   §1 does promise an embedding, not just the value.
4. **Terse proofs of real steps.** Lemma 1 ("follows inductively"), Lemma 2's child-replacement
   step, §5's "every path from outside the child enters through one of its two boundary faces",
   and Lemma 3's "the branch does not enclose $B$" are all correct but each hides a short argument.
   A referee would ask for all four to be written out. A cleaner replacement for Lemma 2 exists and
   I verified it computationally: $\ell(H)$ is the minimum $s$–$t$ edge cut of $H$, manifestly
   embedding-independent.
5. **Edge cases.** $k=0$ (edgeless graph) is a declared convention, not forced by the problem;
   the OPG definition presupposes $k>0$, and the writeup offers both readings. Isolated vertices,
   bridges (whose two incident faces coincide), disconnected graphs and parallel edges are all
   handled and correct; disconnected graphs are argued but not machine-checked here.
6. **Complexity.** $O(N^8)$ is described as "intentionally coarse" and the per-node counts are
   asserted rather than itemized. Polynomiality is not in doubt — the only quantity that could
   have been exponential, the P-node bin capacity $\Lambda$, is bounded by $|E(H)|$ and this is
   noted explicitly ("The lengths here are not arbitrary binary-encoded numbers").
7. **Scope of my verification.** Brute force was limited to graphs with at most ~9 vertices and at
   most ~30000 rotation systems, and to optima $\le3$. A defect appearing only at larger depth
   would not have been caught, though nothing in the structure of the argument suggests one.

## Referee summary

I set out to break this writeup and could not. The architecture is sound and, unusually for a
single-pass proof, the delicate points are the ones the author actually defended: the profile
$F_H(d)$ is legitimate because a pertinent component communicates with the rest of the dual only
through its two boundary faces and because its terminal distance $\ell(H)$ is an embedding
invariant (in fact the $s$–$t$ min cut of $H$, which I confirmed on 412 instances); the P-node
"two-bin" scheduler is not a greedy heuristic but an exact DP whose only exchange property is
proved in full and which I could not break on 8000 synthetic instances or 173 real compositions;
the DP state is a single integer bounded by the number of edges, so there is no hidden exponential;
S, P, Q and R nodes are all covered, with the R-node reflection correctly implemented as a swap of
the two terminal labels; and the cut-vertex reduction, which the author singles out as the
subtle part, is a correct weighted gluing lemma whose lower bound properly handles nested branches.
Every recurrence reproduced brute force over all genus-0 rotation systems in ~13000 test cases,
including a full end-to-end pipeline on 95 random planar graphs and 11 hand-built stress cases.
The residual defects are expositional: four one-line proofs that need writing out, an unargued
sentence about loops, and an unproved (but routine) reconstruction claim — all repairable, none
load-bearing. The reason this is not CONFIRMED is priority, not correctness: Hantao Yu's
arXiv:2607.08110, posted 9 July 2026, already proves exactly this theorem — resolving Bentz's
question by a gadget reduction to minimum face-depth rather than by an SPQR dynamic program — and
its Lemma 3.2 is the same peeling identity the writeup calls Lemma 1. The catalog's "open" status
is simply two months stale. Verdict: **ALREADY_KNOWN**; the writeup is best described as a correct,
independent, and methodologically different second proof of a recently published theorem.
