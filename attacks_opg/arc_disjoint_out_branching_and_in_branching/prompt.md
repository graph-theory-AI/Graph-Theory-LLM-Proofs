Attack the following open graph-theory problem.

Catalog id: arc_disjoint_out_branching_and_in_branching
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/arc_disjoint_out_branching_and_in_branching/
Original entry: http://www.openproblemgarden.org/op/arc_disjoint_out_branching_and_in_branching
Problem attributed to: Thomassen, Carsten (posted 2013-03-02)

=== Problem statement (OpenProblemGarden) ===
Title: Arc-disjoint out-branching and in-branching
Conjecture There exists an integer $ k $ such that every $ k $ -arc-strong digraph $ D $ with specified vertices $ u $ and $ v $ contains an out-branching rooted at $ u $ and an in-branching rooted at $ v $ which are arc-disjoint.

=== Discussion / context (OpenProblemGarden) ===
Thomassen [T] showed that, given a digraph $ D $ and two vertices $ u $ and $ v $ , deciding whether there are an out-branching rooted at $ u $ and an in-branching rooted at $ v $ which are arc-disjoint is NP-complete. In contrast, one can decide in polynomial time whether there are $ k $ arc-disjoint out-branchings with specified roots $ s_1, \dots , s_k $ (some of which may be identical). This is a consequence of Edmonds’ well known branching theorem [E] states that a digraph $ D $ has $ k $ arc-disjoint out-branchings rooted at some fixed vertex $ s $ if and only if there are $ k $ arc-disjoint paths from $ s $ to every other vertex of $ D $ . Bang-Jensen [B] proved this conjecture for tournaments. A similar question can be asked about arc-disjoint strongly connected spanning subdigraphs . Several related problems are mentioned in the survey of Bang-Jensen and Kriesell [BK].

=== References listed by OpenProblemGarden ===
- [B] J. Bang-Jensen, Edge-disjoint in- and out-branching in tournaments and related path problems. J. Combin. Theory Ser. B 51 (1991), 1-23.
- [BK] J. Bang-Jensen, M. Kriesell, Disjoint sub(di)graphs in digraphs, Electronic Notes in Discrete Mathematics 34 (2009), 179-183.
- [E] J. Edmonds, Edge-disjoint branchings. In Combinatorial Algorithms, B. Rustin, ed., Acad. Press, New York (1973), 91-96.
- *[T] C. Thomassen, Configurations in Graphs, Annals of The New York Acad. Sci. 555 (1989), 402-412.

=== Catalog page (statement + literature review) ===
Arc-disjoint out-branching and in-branching — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The general Thomassen conjecture — that some universal $k$ suffices for all digraphs — remains open. Since 2013, the conjecture has been verified for digraphs of independence number at most 2 (where $k=2$ suffices), for semicomplete digraphs (complete classification of which pairs of roots admit a good pair), and for semicomplete compositions; separately, extremal work showed the smallest 2-arc-strong digraph without a good pair has at least 10 vertices.

 Cited literature (5)

 
 
 
partial Arc-disjoint in- and out-branchings in digraphs of independence number at most 2
 (2022)
 

 
 Joergen Bang-Jensen, Stephane Bessy, Frederic Havet, Anders Yeo · Journal of Graph Theory · arXiv:2003.02107 · doi:10.1002/jgt.22779

Every digraph with independence number at most 2 and arc-connectivity at least 2 has an arc-disjoint out-branching and in-branching (i.e., $k=2$ suffices for this class), settling Thomassen's conjecture for digraphs of independence number 2.
 

 
 
partial The smallest number of vertices in a 2-arc-strong digraph which has no good pair
 (2022)
 

 
 Ran Gu, Gregory Gutin, Shasha Li, Yongtang Shi, Zhenyu Taoqiu · Theoretical Computer Science · arXiv:2012.03742

Every 2-arc-strong digraph on at most 9 vertices has a good pair (arc-disjoint out- and in-branching), so any 2-arc-strong counterexample to the conjecture with $k=2$ requires at least 10 vertices.
 

 
 
partial Arc-disjoint out-branchings and in-branchings in semicomplete digraphs
 (2024)
 

 
 Joergen Bang-Jensen, Yun Wang · Journal of Graph Theory · arXiv:2302.06177 · doi:10.1002/jgt.23072

Provides a complete polynomial-time decidable characterisation of which semicomplete digraphs contain a good $(u,v)$-pair for prescribed roots, generalising the 1991 tournament result of Bang-Jensen and confirming a conjecture of Bang-Jensen for semicomplete digraphs.
 

 
 
partial Arc-disjoint out- and in-branchings in compositions of digraphs
 (2024)
 

 
 Joergen Bang-Jensen, Yun Wang · European Journal of Combinatorics · arXiv:2302.08283

Completely solves (in polynomial time) the good-pair problem for semicomplete compositions, extending the semicomplete-digraph classification to a broader class.
 

 
 
partial Strong arc decompositions of split digraphs
 (2025)
 

 
 Joergen Bang-Jensen, Yun Wang · Journal of Graph Theory · arXiv:2309.06904 · doi:10.1002/jgt.23157

Proves that every 3-arc-strong split digraph has a strong arc decomposition (partition of arcs into two strong spanning subdigraphs), which implies good pairs exist in this class; also shows 2-arc-strong is insufficient in general for split digraphs.
 

 

 Reviewer notes. The Wiley (JGT) and ScienceDirect pages returned HTTP 403 and could not be fetched directly; DOIs 10.1002/jgt.22779 and 10.1002/jgt.23072 are taken from Wiley URL patterns visible in search results and are reported with medium confidence. The DOI for arXiv:2302.08283 (European J. Combinatorics) and arXiv:2012.03742 (Theoretical Computer Science) could not be confirmed and are set to null. The conjecture for general digraphs remains open as of all verified sources. The 2019 paper arXiv:1906.08052 (Gutin, Sun) addresses the same-root variant (u=v) and was not included in since_posted as it is tangential to Thomassen's conjecture. No paper was found that resolves the general conjecture.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 183s.
 

Conjecture. There exists an integer $ k $ such that every $ k $ -arc-strong digraph $ D $ with specified vertices $ u $ and $ v $ contains an out-branching rooted at $ u $ and an in-branching rooted at $ v $ which are arc-disjoint.

Discussion

Thomassen [T] showed that, given a digraph $ D $ and two vertices $ u $ and $ v $ , deciding whether there are an out-branching rooted at $ u $ and an in-branching rooted at $ v $ which are arc-disjoint is NP-complete. In contrast, one can decide in polynomial time whether there are $ k $ arc-disjoint out-branchings with specified roots $ s_1, \dots , s_k $ (some of which may be identical). This is a consequence of Edmonds’ well known branching theorem [E] states that a digraph $ D $ has $ k $ arc-disjoint out-branchings rooted at some fixed vertex $ s $ if and only if there are $ k $ arc-disjoint paths from $ s $ to every other vertex of $ D $ . Bang-Jensen [B] proved this conjecture for tournaments. A similar question can be asked about arc-disjoint strongly connected spanning subdigraphs . Several related problems are mentioned in the survey of Bang-Jensen and Kriesell [BK].

Bibliography

 [B]
 J. Bang-Jensen, Edge-disjoint in- and out-branching in tournaments and related path problems. J. Combin. Theory Ser. B 51 (1991), 1-23.

 [BK]
 J. Bang-Jensen, M. Kriesell, Disjoint sub(di)graphs in digraphs, Electronic Notes in Discrete Mathematics 34 (2009), 179-183.

 [E]
 J. Edmonds, Edge-disjoint branchings. In Combinatorial Algorithms, B. Rustin, ed., Acad. Press, New York (1973), 91-96.

★ [T]
 C. Thomassen, Configurations in Graphs, Annals of The New York Acad. Sci. 555 (1989), 402-412.

Related conjectures

 
 implied by
 Arc-disjoint strongly connected spanning subdigraphs
 partial
 Suppose k witnesses the source conjecture, and let D be a k-arc-strong digraph with specified vertices u, v. Then D contains arc-disjoint strongly connected spanning subdigraphs D1 and D2. Any strong spanning subdigraph contains, for every choice of root, both an out-branching and an in-branching (take a BFS out-tree from the root, resp. an in-tree to the root, which exist by strong connectivity and spanning-ness). Take an out-branching rooted at u inside D1 and an in-branching rooted at v inside D2; they are arc-disjoint because D1 and D2 are. Hence the same k witnesses the target conjecture. Both OPG pages cross-reference each other as similar questions but the implication in this direction is rigorous and self-contained.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
