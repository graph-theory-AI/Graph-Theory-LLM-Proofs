Attack the following open graph-theory problem.

Catalog id: shannon_capacity_of_the_seven_cycle
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/shannon_capacity_of_the_seven_cycle/
Original entry: http://www.openproblemgarden.org/op/shannon_capacity_of_the_seven_cycle

=== Problem statement (OpenProblemGarden) ===
Title: Shannon capacity of the seven-cycle
Problem What is the Shannon capacity of $ C_7 $ ?

=== Discussion / context (OpenProblemGarden) ===
Let $ \alpha(G) $ denote the independence number of the graph $ G $ , and let $ G*H $ denote the strong graph product of $ G $ and $ H $ (in which $ (g,h) $ is adjacent to $ (g',h') $ if $ g=g' $ and $ h $ is adjacent to $ h' $ , or if $ h=h' $ and $ g $ is adjacent to $ g' $ , or if $ g $ is adjacent to $ g' $ and $ h $ is adjacent to $ h' $ ). Then the Shannon capacity of $ G $ is defined by $$\theta(G) = \lim_{k\to\infty} \biggl({\alpha(G*G*\cdots*G) \over k}\biggr)^{1/k},$$ where the strong graph product is over $ k $ copies of $ G $ . The Shannon capacity is important because it represents the effective size of an alphabet in a communication model represented by $ G $ , but it is notoriously difficult to compute. Lovász [L] famously proved that the Shannon capacity of the five-cycle $ C_5 $ is $ \sqrt{5} $ , but even the Shannon capacity of $ C_7 $ remains unknown. However, Bohman [B] has shown that $$\lim_{k\to\infty}(k+(1/2)-\theta(C_{2k+1}))=0.$$

=== References listed by OpenProblemGarden ===
- [B] Tom Bohman, A limit theorem for the Shannon capacity of odd cycles II, Proc. Amer. Math. Soc. 133 (2005), no. 2, 537-543.
- [L] László Lovász, On the Shannon capacity of a graph, IEEE Trans. Inform. Th. IT-25 (1979), 1-7.

=== Catalog page (statement + literature review) ===
Shannon capacity of the seven-cycle — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Shannon capacity of $C_7$ remains unknown. Since the problem was posted in 2009, the best lower bound has been improved twice: first to $c(C_7) \geq 350^{1/5} > 3.2271$ by Mathew and Östergård (2016) using stochastic search, and then to $\Theta(C_7) \geq 367^{1/5} > 3.2578$ by Polak and Schrijver (2019) via circular graphs. The Lovász upper bound $\vartheta(C_7) = 7\cos(\pi/7)/(1+\cos(\pi/7)) \approx 3.3177$ remains unmatched, and the exact value is still open.

 Cited literature (2)

 
 
 
partial New Lower Bounds for the Shannon Capacity of Odd Cycles
 (2016)
 

 
 K. Ashik Mathew, Patric R. J. Östergård · Designs, Codes and Cryptography · arXiv:1504.01472 · doi:10.1007/s10623-016-0194-7

Proved $c(C_7) \geq 350^{1/5} > 3.2271$ by computing $\alpha(C_7^5) \geq 350$ using stochastic search with prescribed stabilizers.
 

 
 
partial New lower bound on the Shannon capacity of C7 from circular graphs
 (2019)
 

 
 Sven Polak, Alexander Schrijver · Information Processing Letters · arXiv:1808.07438

Proved $\Theta(C_7) \geq 367^{1/5} > 3.2578$ by constructing an independent set of size 367 in $C_7^{\boxtimes 5}$ via a circulant structure in $\mathbb{Z}_{382}^5$; this is the current best lower bound.
 

 

 Reviewer notes. The exact value of $\Theta(C_7)$ is still open as of May 2026; the gap $367^{1/5} \approx 3.2578 \leq \Theta(C_7) \leq \vartheta(C_7) \approx 3.3177$ has not been closed. A 2025 paper by Zhu (arXiv:2402.10025) improves bounds on the Shannon capacity of *complements* of odd cycles, a related but distinct problem. The 2025 survey by Lavi and Sason (arXiv:2509.24600) covers advances for other graph families (q-Kneser, tadpole) but contains no new results on $C_7$. The 2023 Mycielski paper (arXiv:2312.09224) is about a different construction and does not resolve $C_7$.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Problem. What is the Shannon capacity of $ C_7 $ ?

Discussion

Let $ \alpha(G) $ denote the independence number of the graph $ G $ , and let $ G*H $ denote the strong graph product of $ G $ and $ H $ (in which $ (g,h) $ is adjacent to $ (g',h') $ if $ g=g' $ and $ h $ is adjacent to $ h' $ , or if $ h=h' $ and $ g $ is adjacent to $ g' $ , or if $ g $ is adjacent to $ g' $ and $ h $ is adjacent to $ h' $ ). Then the Shannon capacity of $ G $ is defined by $$\theta(G) = \lim_{k\to\infty} \biggl({\alpha(G*G*\cdots*G) \over k}\biggr)^{1/k},$$ where the strong graph product is over $ k $ copies of $ G $ . The Shannon capacity is important because it represents the effective size of an alphabet in a communication model represented by $ G $ , but it is notoriously difficult to compute. Lovász [L] famously proved that the Shannon capacity of the five-cycle $ C_5 $ is $ \sqrt{5} $ , but even the Shannon capacity of $ C_7 $ remains unknown. However, Bohman [B] has shown that $$\lim_{k\to\infty}(k+(1/2)-\theta(C_{2k+1}))=0.$$

Bibliography

 [B]
 Tom Bohman, A limit theorem for the Shannon capacity of odd cycles II, Proc. Amer. Math. Soc. 133 (2005), no. 2, 537-543.

 [L]
 László Lovász, On the Shannon capacity of a graph, IEEE Trans. Inform. Th. IT-25 (1979), 1-7.
