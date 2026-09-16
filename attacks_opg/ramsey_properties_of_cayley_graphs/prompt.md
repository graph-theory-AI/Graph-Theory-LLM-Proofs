Attack the following open graph-theory problem.

Catalog id: ramsey_properties_of_cayley_graphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Algebraic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/ramsey_properties_of_cayley_graphs/
Original entry: http://www.openproblemgarden.org/op/ramsey_properties_of_cayley_graphs
Problem attributed to: Alon, Noga (posted 2007-06-10)

=== Problem statement (OpenProblemGarden) ===
Title: Ramsey properties of Cayley graphs
Conjecture There exists a fixed constant $ c $ so that every abelian group $ G $ has a subset $ S \subseteq G $ with $ -S = S $ so that the Cayley graph $ {\mathit Cayley}(G,S) $ has no clique or independent set of size $ > c \log |G| $ .

=== Discussion / context (OpenProblemGarden) ===
The classic bounds from Ramsey theory show that every $ n $ vertex graph must have either a clique or an independent set of size $ c \log n $ and further random graphs almost surely have this property (using different values of $ c $ ). The above conjecture asserts that every group has a Cayley graph with similar behavior. Improving upon some earlier results of Agarwal et. al. [AAAS], Green [G] proved that there exists a constant $ c $ so that whenever a set $ S \subseteq {\mathbb Z}_n $ is chosen at random, and we form the graph with vertex set $ {\mathbb Z}_n $ and two vertices $ i $ , $ j $ joined if $ i+j \in S $ , then this graph almost surely has both maximum clique size and maximum independent size $ O(\log n) $ . The reader should note that such graphs are not generally Cayley graphs - although the definition is similar. As a word of caution, Green [G] also shows that a randomly chosen subset of the group $ {\mathbb Z}_2^n $ almost surely has both max. clique and max. independent set of size $ \Theta( \log N \log \log N ) $ where $ N = 2^n $ .

=== References listed by OpenProblemGarden ===
- [AAAS] P. K. Agarwal, N. Alon, B. Aronov, S. Suri, Can visibility graphs be represented compactly? Discrete Comput. Geom. 12 (1994), no. 3, 347--365. MathSciNet
- *[C] Problem BCC14.6 from the BCC Problem List (edited by Peter Cameron)
- [G] B. Green, Counting sets with small sumset, and the clique number of random Cayley graphs, Combinatorica 25 (2005), no. 3, 307--326. MathSciNet

=== Catalog page (statement + literature review) ===
Ramsey properties of Cayley graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Alon's conjecture — that every abelian group $G$ has a Cayley graph with no clique or independent set of size $> c\log|G|$ — remains open in full generality, but major progress was made in December 2024. Conlon, Fox, Pham, and Yepremyan proved the conjecture for all abelian groups of order $N$ for almost all $N$, and also constructed self-complementary Ramsey Cayley graphs on finite vector spaces of characteristic $\equiv 1\pmod{4}$ with clique and independence numbers $\leq (2+o(1))\log N$.

 Cited literature (2)

 
 
 
partial On the clique number of random Cayley graphs and related topics
 (2024)
 

 
 David Conlon, Jacob Fox, Huy Tuan Pham, Liana Yepremyan · arXiv preprint · arXiv:2412.21194

Proves Alon's conjecture for all abelian groups of order N for almost all N; for vector spaces with characteristic ≡ 1 (mod 4) constructs self-complementary Cayley graphs with clique and independence number ≤ (2+o(1)) log N; also improves the random Cayley clique-number upper bound from O(log² N) to O(log N log log N).
 

 
 
partial On the clique number of random Cayley graphs and related topics
 (2024)
 

 
 David Conlon, Jacob Fox, Huy Tuan Pham, Liana Yepremyan · arXiv preprint · arXiv:2412.21194

Proves Alon's conjecture for all abelian groups of order $N$ for almost all $N$; additionally, for finite vector spaces of order $N$ with characteristic $\equiv 1\pmod{4}$, proves the existence of a self-complementary Cayley graph with clique number and independence number both at most $(2+o(1))\log N$.
 

 

 Reviewer notes. arXiv:2412.21194 (Conlon–Fox–Pham–Yepremyan, Dec 2024) is the key post-posting result; it resolves the conjecture for 'almost all N' but leaves open whether every abelian group of every order has a Ramsey Cayley graph. The companion paper arXiv:2509.02561 (Alon–Pham, Sep 2025) studies random sumsets and independence numbers in sparse Cayley graphs but does not directly address the full conjecture. The conjecture for non-abelian groups and for all abelian groups unconditionally remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. There exists a fixed constant $ c $ so that every abelian group $ G $ has a subset $ S \subseteq G $ with $ -S = S $ so that the Cayley graph $ {\mathit Cayley}(G,S) $ has no clique or independent set of size $ > c \log |G| $ .

Keywords:
Cayley graph · Ramsey number

Discussion

The classic bounds from Ramsey theory show that every $ n $ vertex graph must have either a clique or an independent set of size $ c \log n $ and further random graphs almost surely have this property (using different values of $ c $ ). The above conjecture asserts that every group has a Cayley graph with similar behavior. Improving upon some earlier results of Agarwal et. al. [AAAS], Green [G] proved that there exists a constant $ c $ so that whenever a set $ S \subseteq {\mathbb Z}_n $ is chosen at random, and we form the graph with vertex set $ {\mathbb Z}_n $ and two vertices $ i $ , $ j $ joined if $ i+j \in S $ , then this graph almost surely has both maximum clique size and maximum independent size $ O(\log n) $ . The reader should note that such graphs are not generally Cayley graphs - although the definition is similar. As a word of caution, Green [G] also shows that a randomly chosen subset of the group $ {\mathbb Z}_2^n $ almost surely has both max. clique and max. independent set of size $ \Theta( \log N \log \log N ) $ where $ N = 2^n $ .

Bibliography

 [AAAS]
 P. K. Agarwal, N. Alon, B. Aronov, S. Suri, Can visibility graphs be represented compactly? Discrete Comput. Geom. 12 (1994), no. 3, 347--365. MathSciNet
 Can visibility graphs be represented compactly? · MathSciNet

★ [C]
 Problem BCC14.6 from the BCC Problem List (edited by Peter Cameron)
 BCC Problem List

 [G]
 B. Green, Counting sets with small sumset, and the clique number of random Cayley graphs , Combinatorica 25 (2005), no. 3, 307--326. MathSciNet
 Counting sets with small sumset, and the clique number of random Cayley graphs · MathSciNet
