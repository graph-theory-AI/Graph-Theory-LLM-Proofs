Attack the following open graph-theory problem.

Catalog id: 1611.03196__00
Catalog status: open (triage tier 3, lean disprove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1611.03196__00/
Source paper: Fair representation by independent sets (arXiv:1611.03196)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.6
Given a partition of the vertex set of a path into sets $V_1, \ldots, V_m$ there exists an independent set $S$ and integers $b_i$, $i \leq m$, such that $|S \cap V_i| \geq \frac{|V_i|}{2} - b_i$ for all $i$, and 1. $\sum_{i \leq m} b_i \leq \frac{m}{2}$ and 2. $b_i \leq 1$ for all $i \leq m$.

Context:
The paper proves (Theorem 1.7) that either condition alone holds for the independence complex of a path, but not necessarily both simultaneously. Conjecture 1.6 asserts both conditions can be satisfied at once. The matching complex of a path is the independence complex of a path one vertex shorter.

=== Catalog page (statement + literature review) ===
Simultaneous fair representation in path partitions — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No follow-up paper was found that resolves the full statement of Conjecture 1.6 from arXiv:1611.03196, which asks for an independent set in a partitioned path satisfying both the global budget condition (sum b_i ≤ m/2) and the per-part cap (b_i ≤ 1) simultaneously. Related work has appeared on fair representation in cycles (computational complexity, PPA-completeness) and sparse graphs, but these address different graph classes. Alishahi and Meunier (2017, arXiv:1704.02921) proved 'a conjecture of Ron Aharoni and coauthors' about colored paths, but this could not be confirmed to be specifically Conjecture 1.6; it may instead resolve a different conjecture from the same paper.

 Cited literature (1)

 
 
 
partial Fair splitting of colored paths
 (2017)
 

 
 Meysam Alishahi, Frédéric Meunier · arXiv preprint · arXiv:1704.02921

Proves 'a conjecture of Ron Aharoni and coauthors' about fair splitting of colored paths into two disjoint independent sets, but which specific conjecture from arXiv:1611.03196 this resolves could not be confirmed; it may be a different conjecture from the same paper rather than Conjecture 1.6.
 

 

 Reviewer notes. Conjecture 1.6 is a joint condition combining two separately-provable bounds (Theorem 1.7 of the source paper). Related literature has grown around cycles and sparse graphs (fair representation in cycles, PPA-completeness of finding such sets), but no paper explicitly claiming to prove or disprove Conjecture 1.6 for paths was found. The conjecture is 9 years old, so medium rather than high confidence in 'open' status.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Given a partition of the vertex set of a path into sets $V_1, \ldots, V_m$ there exists an independent set $S$ and integers $b_i$, $i \leq m$, such that $|S \cap V_i| \geq \frac{|V_i|}{2} - b_i$ for all $i$, and 1. $\sum_{i \leq m} b_i \leq \frac{m}{2}$ and 2. $b_i \leq 1$ for all $i \leq m$.

Context

The paper proves (Theorem 1.7) that either condition alone holds for the independence complex of a path, but not necessarily both simultaneously. Conjecture 1.6 asserts both conditions can be satisfied at once. The matching complex of a path is the independence complex of a path one vertex shorter.

Notes. PDF source — sum symbol garbled as (cid:80) and fractions may be garbled; LaTeX reconstructed from context.

Source paper

 Fair representation by independent sets
 Ron Aharoni, Noga Alon, Eli Berger, Maria Chudnovsky, Dani Kotlar, Martin Loebl, Ran Ziv · 2016-11-10
 https://arxiv.org/abs/1611.03196
 PDF source

=== Source paper abstract / header ===
Abstract:For a hypergraph $H$ let $\beta(H)$ denote the minimal number of edges from $H$ covering $V(H)$. An edge $S$ of $H$ is said to represent {\em fairly} (resp. {\em almost fairly}) a partition $(V_1,V_2, \ldots, V_m)$ of $V(H)$ if $|S\cap V_i|\ge \lfloor\frac{|V_i|}{\beta(H)}\rfloor$ (resp. $|S\cap V_i|\ge \lfloor\frac{|V_i|}{\beta(H)}\rfloor-1$) for all $i \le m$.
In matroids any partition of $V(H)$ can be represented fairly by some independent set. We look for classes of hypergraphs $H$ in which any partition of $V(H)$ can be represented almost fairly by some edge.
We show that this is true when $H$ is the set of independent sets in a path, and conjecture that it is true when $H$ is the set of matchings in $K_{n,n}$. We prove that partitions of $E(K_{n,n})$ into three sets can be represented almost fairly. The methods of proofs are topological.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1611.03196 [math.CO]
 

 
  
 (or 
 arXiv:1611.03196v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1611.03196
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Daniel Kotlar [view email] 
 [v1]
 Thu, 10 Nov 2016 06:31:33 UTC (276 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Fair representation by independent sets, by Ron Aharoni and 6 other authors
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
 | 2016-11
 

 Change to browse by:
 
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
The problem above was already attacked by `gpt-5.6-sol`, which reported verdict `disproved` at high confidence. That attempt is reproduced below.
An adversarial referee then reviewed it and returned `FATAL_ERROR`, i.e. the claimed resolution did not stand, so the problem is still open.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "With the stated requirement that the b_i are integers, the partition V_1={2,4,6}, V_2={1}, V_3={3,5,7} of P_7 is a counterexample.",
  "would_publish": false,
  "caveats": "The counterexample relies essentially on integrality; the original conjecture may instead allow real b_i, in which case this does not apply."
}
```

## Statement under consideration

Let \(P\) be a path whose vertex set is partitioned into \(V_1,\dots,V_m\). The stated conjecture asks for an independent set \(S\) and integers \(b_1,\dots,b_m\) satisfying
\[
|S\cap V_i|\ge \frac{|V_i|}{2}-b_i,\qquad b_i\le 1,
\]
and
\[
\sum_{i=1}^m b_i\le \frac m2.
\]

No lower bound on the \(b_i\) is needed for the counterexample below.

## Counterexample

Take the path
\[
P_7=1-2-3-4-5-6-7
\]
and partition its vertices into three nonempty classes
\[
V_1=\{2,4,6\},\qquad V_2=\{1\},\qquad V_3=\{3,5,7\}.
\]
Thus \(m=3\), and every class has odd cardinality.

Suppose that \(S\) and integers \(b_1,b_2,b_3\) satisfy the conjectured inequalities. Since \(b_i\) is integral, from
\[
|S\cap V_i|\ge \frac{|V_i|}{2}-b_i
\]
we obtain
\[
b_i\ge \left\lceil\frac{|V_i|}{2}\right\rceil-|S\cap V_i|.
\]
Summing over \(i\) gives
\[
\sum_{i=1}^3 b_i
 \ge
\sum_{i=1}^3\left\lceil\frac{|V_i|}{2}\right\rceil-|S|
 = (2+1+2)-|S|
 =5-|S|.
\]
On the other hand, \(\sum_i b_i\) is an integer and
\[
\sum_i b_i\le \frac32,
\]
so in fact
\[
\sum_i b_i\le 1.
\]
Consequently
\[
5-|S|\le 1,
\]
and hence
\[
|S|\ge4.
\]

The independence number of \(P_7\) is \(4\), and its unique independent set of cardinality \(4\) is
\[
S=\{1,3,5,7\}.
\]
Indeed, if \(x_1<x_2<x_3<x_4\) are four pairwise nonconsecutive vertices of \(P_7\), then
\[
x_4\ge x_1+6\ge7,
\]
forcing \(x_1=1\) and all three gaps to equal \(2\).

Thus any candidate \(S\) must equal \(\{1,3,5,7\}\). In particular,
\[
|S\cap V_1|=0.
\]
But \(|V_1|=3\) and \(b_1\le1\), so the required inequality would imply
\[
0=|S\cap V_1|
 \ge \frac32-b_1
 \ge \frac12,
\]
a contradiction.

Therefore the conjecture, as stated with **integer** \(b_i\), is false.

## Integrality caveat

The argument uses the rounding consequence
\[
b_i\ge \left\lceil |V_i|/2\right\rceil-|S\cap V_i|.
\]
It does not disprove the version in which the \(b_i\) are arbitrary real numbers. For example, in the displayed partition, the independent set
\[
S=\{2,5\}
\]
works for the real-valued version with
\[
b_1=b_2=b_3=\frac12.
\]
Thus the original source should be checked carefully: if it says “numbers” rather than “integers,” the catalog extraction has materially strengthened the conjecture, and the genuine real-valued problem remains untouched by this counterexample.

--- referee report on that attempt ---
---
id: 1611.03196__00
claimed_verdict: disproved
review_verdict: FATAL_ERROR
confidence: high
interpretation_ok: false
references_ok: true
computation_run: true
one_line: The P_7 counterexample is arithmetically correct but only refutes a rounding artifact of the literal "integer b_i" wording; the intended Conjecture 1.6, as read and cited explicitly by Alishahi-Meunier (EJC 2017), was PROVED by them in 2017, so the "disproved" verdict is untenable.
---

## Interpretation

The catalog extraction is verbatim faithful to the source. I downloaded the arXiv v1
TeX (`arxiv.org/e-print/1611.03196`, file `fairrep_nov_10.tex`); Conjecture 1.6
(label `treesconj0`) reads exactly:

> Given a partition of the vertex set of a path into sets $V_1,\ldots,V_m$ there
> exists an independent set $S$ and **integers** $b_i$, $i\le m$, such that
> $|S\cap V_i| \ge \frac{|V_i|}{2} - b_i$ for all $i$, and
> (1) $\sum_{i\le m} b_i \le \frac m2$ and (2) $b_i \le 1$ for all $i\le m$.

So the "integers" and the un-floored $\frac{|V_i|}{2}$ are in the original, not a
catalog garbling (the writeup's caveat guessed the opposite failure mode).

However, the writeup's verdict rests entirely on the integrality of $b_i$, and that
is a drafting artifact, not the intended content. Evidence:

1. **The paper's own framing.** Conjecture 1.6 is introduced as "a slightly
   stronger form" of the (proved) statement that the independence complex of a path
   admits *almost fair* representation, i.e. $|S\cap V_i| \ge \lfloor|V_i|/2\rfloor - 1$.
   On odd parts the true deficit $|V_i|/2 - |S\cap V_i|$ is a half-integer, which an
   integer $b_i$ cannot express; the literal wording silently converts a deficit of
   $1/2$ into a cost of $1$ against the budget $m/2$. The writeup's counterexample
   lives entirely inside this rounding gap (all three parts odd).

2. **How the field reads Conjecture 1.6.** Alishahi and Meunier, "Fair splitting of
   colored paths" (arXiv:1704.02921; published, peer-reviewed, Electron. J. Combin.
   24(3) #P3.41, 2017), cite it as `\cite[Conjecture 1.6]{aharoni2016fair}` and
   restate it as: *there always exists an independent set $S$ with
   $|S\cap V_j| \ge |V_j|/2 - 1$ for all $j$, with strict inequality for at least
   $m/2$ of the $V_j$.* On even parts this is exactly the integer-$b_i$ statement;
   on odd parts it is the sensible (half-integer-aware) reading. **They then prove
   it** (their Theorem 1: one can delete one vertex per class and split the rest of
   the path into two independent sets $S_1, S_2$ with
   $|S_i\cap V_j| \ge |V_j|/2 - 1$; since $|S_1\cap V_j|+|S_2\cap V_j| = |V_j|-1$,
   one of the two is strict on at least $m/2$ classes), stating explicitly
   "Theorem 1 implies in particular that the conjecture by Aharoni et al. is true."
   Later literature (e.g. Haviv, ITCS 2021, on cycles) likewise formulates fairness
   as $|S\cap V_i| \ge |V_i|/2 - 1$, never via integer budget variables.

3. **A 7-vertex counterexample would not have escaped seven authors** (including
   Alon and Chudnovsky) who in the same paper prove each condition separately; the
   only coherent explanation is that the integer phrasing does not carry their
   intent on odd parts.

Would a reasonable author of the original paper consider their conjecture resolved
by this writeup? **No.** They would consider it resolved — affirmatively — by
Alishahi–Meunier (2017), and would regard the P_7 example as exposing a wording
infelicity, not refuting the conjecture. This is precisely the "interpretation
gaming" failure mode: a strawman-literal reading is refuted while the intended
statement is in fact a theorem in the literature. (The writeup itself half-knew
this: `would_publish: false` and a caveat that the counterexample "relies
essentially on integrality"; but its guess that the paper might say "numbers" was
wrong, and it missed that the intended reading is already proved.)

Note also that the catalog's "open" status is itself wrong: the Alishahi–Meunier
paper flagged as "partial/unconfirmed" in the catalog does resolve Conjecture 1.6
specifically — their citation `[Conjecture 1.6]{aharoni2016fair}` is explicit in
their TeX.

## Step-by-step findings

Steps refer to the writeup's counterexample argument (P_7 with $V_1=\{2,4,6\}$,
$V_2=\{1\}$, $V_3=\{3,5,7\}$, $m=3$).

| step | label | note |
|------|-------|------|
| S1. From $b_i$ integral, $b_i \ge \lceil |V_i|/2 \rceil - |S\cap V_i|$ | VALID | Minimal integer $b_i$ satisfying $|S\cap V_i|\ge |V_i|/2-b_i$ is $\lceil |V_i|/2 - |S\cap V_i| \rceil = \lceil |V_i|/2\rceil - |S\cap V_i|$ (intersection is an integer). Negative $b_i$ are allowed and only help the sum; the bound is per-part and correct. |
| S2. Summing: $\sum b_i \ge (2+1+2) - |S| = 5 - |S|$ | VALID | $\lceil 3/2\rceil + \lceil 1/2\rceil + \lceil 3/2\rceil = 2+1+2 = 5$; $\sum_i |S\cap V_i| = |S|$ since the $V_i$ partition $V(P_7)$. |
| S3. $\sum b_i \le 3/2$ and integral $\Rightarrow \sum b_i \le 1$ | VALID | Sum of integers is an integer; largest integer $\le 3/2$ is $1$. |
| S4. Hence $|S| \ge 4$ | VALID | $5 - |S| \le 1$. |
| S5. $\alpha(P_7)=4$ with unique maximum independent set $\{1,3,5,7\}$ | VALID | Gap argument $x_4 \ge x_1 + 6$ is correct; confirmed by brute force: P_7 has 34 independent sets, exactly one of size 4, none larger. |
| S6. $|S\cap V_1| = 0$ contradicts $0 \ge 3/2 - b_1 \ge 1/2$ given $b_1 \le 1$ | VALID | $\{1,3,5,7\} \cap \{2,4,6\} = \emptyset$; $b_1 \le 1$ forces $3/2 - b_1 \ge 1/2 > 0$. Contradiction stands. |
| S7. Conclusion: literal (integer $b_i$) statement is false | VALID (as a statement about the literal wording) | Independently confirmed by two brute-force methods (see Computational check). But see Interpretation: this does not disprove the intended conjecture. |
| S8. Caveat: real-$b_i$ version satisfied by $S=\{2,5\}$, $b_i = 1/2$ | VALID | Verified: deficits are exactly $(1/2,1/2,1/2)$, sum $3/2 \le 3/2$, each $\le 1$. |
| Verdict block: "disproved", confidence high | ERROR | The headline claim that Conjecture 1.6 is disproved is wrong for the conjecture as intended and as understood in the peer-reviewed literature, where it is a theorem (Alishahi–Meunier 2017). Only a rounding artifact of the arXiv phrasing was refuted. |

## Reference check

- **arXiv:1611.03196 (source paper), Conjecture 1.6 and Theorem 1.7.** Checked
  against the actual TeX source (not just the summarizing fetch). Conjecture 1.6 is
  verbatim as the catalog and writeup state, including "integers $b_i$" and
  un-floored $|V_i|/2$. Theorem 1.7 (`pathscasetotal`) asserts the sum condition
  alone; Theorem 1.8 (`pathscaseindividual`) gives $|S\cap V_i| \ge |V_i|/2 - 1$
  for cycles (the per-part condition alone). The paper says explicitly it proves
  "either condition ... (but not necessarily both simultaneously)". All consistent
  with the prompt. CONFIRMED.
- **arXiv:1704.02921, Alishahi–Meunier, "Fair splitting of colored paths".**
  Checked against its TeX source. It cites Conjecture 1.6 explicitly, restates it
  in the strict-inequality form, and proves it (Theorem 1, via the octahedral
  Tucker lemma). Published: Electron. J. Combin. 24(3), #P3.41, 2017. CONFIRMED —
  and fatal to the writeup's headline verdict.
- The writeup itself cites nothing else. Not checked: whether the published Springer
  version of the source paper (in *A Journey Through Discrete Mathematics*, 2017,
  pp. 31–58) rewords Conjecture 1.6 (paywalled); immaterial given the above.

## Computational check

Script: `verification/scripts/1611.03196__00/check.py`
(pure Python, brute force). Results:

- P_7 has 34 independent sets; exactly one of size 4, namely $\{1,3,5,7\}$, and
  none larger — confirming S5.
- **Literal integer reading, writeup's instance: INFEASIBLE**, verified two ways:
  (a) per-$S$ minimal $b_i = \lceil|V_i|/2\rceil - |S\cap V_i|$ over all 34
  independent sets; (b) fully naive enumeration of all integer vectors
  $b \in \{-7,\dots,1\}^3$ against all 34 sets. Both find no solution. The
  counterexample is correct as stated.
- Real-$b_i$ relaxation: feasible, e.g. $S=\{2,5\}$ with deficits
  $(1/2,1/2,1/2)$ — the writeup's caveat witness checks out exactly.
- Alishahi–Meunier reading: feasible on the instance ($S=\{2,5\}$, all three
  inequalities strict), consistent with their theorem.
- Floor variant $|S\cap V_i| \ge \lfloor|V_i|/2\rfloor - b_i$: also feasible.
- Sweep of **all** set partitions of $P_n$ for $n \le 9$ (877 partitions at $n=7$,
  4140 at $n=8$, 21147 at $n=9$): the literal integer reading fails on 5 partitions
  at $n=7$ (the writeup's pattern: three odd classes; smallest found
  $V_1=\{1,3,5\}, V_2=\{2,4,6\}, V_3=\{7\}$), 0 at $n=8$, 173 at $n=9$; $n=7$ is
  the smallest path with any literal-reading counterexample. On every one of those
  178 failing instances the real, Alishahi–Meunier, and floor readings are all
  satisfiable — confirming that only the integer-rounding artifact ever fails.

## Caveats

- The writeup's mathematics is internally flawless; the failure is entirely at the
  interpretation layer, and the writeup itself hedged (`would_publish: false`,
  integrality caveat) while still stamping "disproved / high confidence" in the
  verdict block.
- The writeup's caveat misdiagnosed the risk: it suggested the paper might say
  "numbers" instead of "integers" (it does say integers); the actual issue is that
  the integer phrasing is a rounding-infelicitous rendering of a half-integer
  deficit condition, as the field's reading (Alishahi–Meunier) shows.
- The catalog status "open (lean disprove)" is itself incorrect: Conjecture 1.6 was
  resolved positively in 2017 by Alishahi–Meunier (EJC 24(3) #P3.41), who cite it
  by number. Any verdict for this target should record the conjecture as
  ALREADY RESOLVED (proved) in the literature.
- If one insists on grading only the literal arXiv v1 string: that statement is
  indeed false, the P_7 example is correct and (per the sweep) smallest possible.
  But no reasonable author would accept that as a disproof of Conjecture 1.6, and
  the writeup's one-line claim announces the conjecture itself as disproved.
- Untested edge cases are not an issue: the counterexample is a single explicit
  instance and was verified exhaustively; $m=3$ is odd, which is where the integer
  budget $\lfloor m/2 \rfloor$ bites hardest.

## Referee summary

The writeup exhibits the partition $V_1=\{2,4,6\}, V_2=\{1\}, V_3=\{3,5,7\}$ of
$P_7$ and argues that no independent set admits integer $b_i \le 1$ with
$\sum b_i \le 3/2$; every step of that argument is correct and I confirmed
infeasibility by exhaustive computation, along with the writeup's claim that the
real-$b_i$ relaxation is satisfiable on the same instance. However, the verdict
"disproved" targets a strawman: the integer phrasing of Conjecture 1.6 in the
arXiv source cannot express the half-integer deficits of odd classes, and the
intended statement — as restated with explicit citation "[Conjecture 1.6]" and
proved by Alishahi and Meunier in a peer-reviewed 2017 paper (Electron. J. Combin.
24(3) #P3.41, via the octahedral Tucker lemma) — is true. The conjecture is
therefore neither open nor disproved: it is a known theorem, and the writeup's
headline claim is fatally wrong even though its arithmetic is impeccable.

