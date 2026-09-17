Attack the following open graph-theory problem.

Catalog id: coloring_random_subgraphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Probabilistic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/coloring_random_subgraphs/
Original entry: http://www.openproblemgarden.org/op/coloring_random_subgraphs
Problem attributed to: Bukh, Boris (posted 2008-06-18)

=== Problem statement (OpenProblemGarden) ===
Title: Coloring random subgraphs
If $ G $ is a graph and $ p \in [0,1] $ , we let $ G_p $ denote a subgraph of $ G $ where each edge of $ G $ appears in $ G_p $ with independently with probability $ p $ . Problem Does there exist a constant $ c $ so that $ {\mathbb E}(\chi(G_{1/2})) > c \frac{\chi(G)}{\log \chi(G)} $ ?

=== Discussion / context (OpenProblemGarden) ===
It is a classical result that the above problem has a positive answer when $ G $ is the complete graph. More generally, the lower bound $ {\mathbb E}(\chi(G_{1/2})) \ge c \frac{\chi(G)}{\log |V(G)|} $ is known. It is easy to obtain the bound $ {\mathbb E}(\chi(G_{1/2})) \ge (\chi(G))^{1/2} $ , since we may imagine forming two random subgraphs $ H,H' $ of $ G $ by putting each edge of $ G $ in either $ H $ or $ H' $ independently with probability $ 1/2 $ . Then $ \chi(H) \chi(H') \ge \chi(G) $ and this gives the desired bound. A similar argument with three subgraphs shows that $ {\mathbb E}(\chi(G_{1/3})) \ge (\chi(G))^{1/3} $ , however these arguments all seem to require integer multiples, so the best known lower bound on $ {\mathbb E}(\chi(G_{49/100})) $ of this form is $ (\chi(G))^{1/3} $ .

=== References listed by OpenProblemGarden ===
- *[B] Boris Bukh's problem page.

=== Catalog page (statement + literature review) ===
Coloring random subgraphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Bukh's 2008 conjecture that $\mathbb{E}(\chi(G_{1/2})) \geq c\,\chi(G)/\log\chi(G)$ for all graphs $G$ remains open. Partial results confirm it for graphs with small independence number $\alpha(G) \leq O(n/k)$ (Shinkar 2016) and for the fractional chromatic number analogue (Mohar–Wu 2018), and a 2023 paper by the original proposer with collaborators establishes tail-probability bounds for $\chi(G_{1/2})$ and studies the degeneracy of $G_{1/2}$, but the conjecture in its original integral form is unresolved.

 Cited literature (5)

 
 
 
partial On Coloring Random Subgraphs of a Fixed Graph
 (2016)
 

 
 Igor Shinkar · arXiv preprint · arXiv:1612.04319

Proves Bukh's conjecture for the special case of graphs with $\chi(G)=k$ and independence number $\alpha(G) \leq O(n/k)$, and gives exponential tail bounds showing $\Pr[\chi(G_{1/2}) \leq d] \leq \exp(-\Omega(k(k-d^3)/d^3))$ for all $d \leq k^{1/3}$.
 

 
 
partial Fractional chromatic number of a random subgraph
 (2018)
 

 
 Bojan Mohar, Hehui Wu · Journal of Graph Theory · arXiv:1807.06285

Proves the fractional-chromatic-number analogue of Bukh's conjecture: for every graph with fractional chromatic number $\geq n$, a random subgraph $G_{1/2}$ has fractional chromatic number $\geq n/(8\log_2(4n))$ with probability $> 1 - 1/(2n)$.
 

 
 
partial Expected Chromatic Number of Random Subgraphs
 (2018)
 

 
 Ross Berkowitz, Pat Devlin, Catherine Lee, Henry Reichard, David Townley · arXiv preprint · arXiv:1811.02018

Establishes a new spectral lower bound on $\mathbb{E}[\chi(G_p)]$ as progress toward Bukh's conjecture, and confirms the conjecture for planar graphs and graphs with chromatic number less than 4.
 

 
 
partial Colouring random subgraphs
 (2023)
 

 
 Boris Bukh, Michael Krivelevich, Bhargav Narayanan · Combinatorics, Probability and Computing · arXiv:2312.08340 · doi:10.1017/S0963548325000069

Proves tail bounds for $\chi(G_{1/2})$ across several regimes, and shows there exist infinitely many $k$-regular graphs whose degeneracy (colouring number) of $G_{1/2}$ is at most $k/3+o(k)$ w.h.p.; explicitly lists the conjecture $\mathbb{E}[\chi(G_{1/2})] = \Omega(k/\log k)$ as an open problem (Problem 1.1).
 

 
 
partial Fractional chromatic number of a random subgraph
 (2018)
 

 
 Bojan Mohar, Hehui Wu · arXiv preprint · arXiv:1807.06285

Proves an affirmative answer to a strengthening of Bukh's question for the fractional chromatic number: for every graph $G$ with $\chi_f(G) \geq t$, the fractional chromatic number of $G_p$ is at least $t/(8\log_{1/p}(et)+4)$ with probability at least $1-1/(2t)$.
 

 

 Reviewer notes. The Wiley journal page for Mohar–Wu (doi:10.1002/jgt.22571) returned HTTP 403; the DOI is inferred from the Wiley URL appearing in search results but was not directly fetch-verified, so it is left null. The 2023/2025 Bukh–Krivelevich–Narayanan paper was verified via both the arXiv abstract page and the Cambridge Core journal page (published CPC vol. 34 iss. 4, 2025). No resolution of the original integer chromatic number conjecture was found through 2026.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 142s.
 

Problem. Does there exist a constant $ c $ so that $ {\mathbb E}(\chi(G_{1/2})) > c \frac{\chi(G)}{\log \chi(G)} $ ?

Keywords:
coloring · random graph

Discussion

It is a classical result that the above problem has a positive answer when $ G $ is the complete graph. More generally, the lower bound $ {\mathbb E}(\chi(G_{1/2})) \ge c \frac{\chi(G)}{\log |V(G)|} $ is known. It is easy to obtain the bound $ {\mathbb E}(\chi(G_{1/2})) \ge (\chi(G))^{1/2} $ , since we may imagine forming two random subgraphs $ H,H' $ of $ G $ by putting each edge of $ G $ in either $ H $ or $ H' $ independently with probability $ 1/2 $ . Then $ \chi(H) \chi(H') \ge \chi(G) $ and this gives the desired bound. A similar argument with three subgraphs shows that $ {\mathbb E}(\chi(G_{1/3})) \ge (\chi(G))^{1/3} $ , however these arguments all seem to require integer multiples, so the best known lower bound on $ {\mathbb E}(\chi(G_{49/100})) $ of this form is $ (\chi(G))^{1/3} $ .

Bibliography

★ [B]
 Boris Bukh's problem page .
 Boris Bukh's problem page
