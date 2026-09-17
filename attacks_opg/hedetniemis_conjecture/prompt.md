Attack the following open graph-theory problem.

Catalog id: hedetniemis_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/hedetniemis_conjecture/
Original entry: http://www.openproblemgarden.org/op/hedetniemis_conjecture
Problem attributed to: Hedetniemi, Stephen T. (posted 2008-05-25)

=== Problem statement (OpenProblemGarden) ===
Title: Hedetniemi's Conjecture
Conjecture If $ G,H $ are simple finite graphs, then $ \chi(G \times H) = \min \{ \chi(G), \chi(H) \} $ . Here $ G \times H $ is the tensor product (also called the direct or categorical product) of $ G $ and $ H $ .

=== Discussion / context (OpenProblemGarden) ===
This beautiful and seemingly innocent conjecture asserts a deep and important property of graph coloring. It is undoubtedly one of the most significant unsolved problems in graph coloring and graph homomorphisms. We write $ G \rightarrow H $ if there is a homomorphism from $ G $ to $ H $ . The graph $ G \times H $ has a two natural projection maps (projecting onto either the first or second coordinate), and these maps are homomorphisms to $ G $ and to $ H $ . So, in short, $ G \times H \rightarrow G $ and $ G \times H \rightarrow H $ . A graph is $ n $ -colorable if and only if it has a homomorphism to $ K_n $ . Combining this with the transitivity of $ \rightarrow $ we find that $ \chi(G \times H) \le \min\{ \chi(G), \chi(H) \} $ (indeed, if $ \chi(G) = n $ , then $ G \times H \rightarrow G $ and $ G \rightarrow K_n $ , so $ G \times H \rightarrow K_n $ - equivalently, $ G \times H $ is $ n $ -colorable). So, the hard direction of Hedetniemi's Conjecture is to prove that $ \chi(G \times H) \ge \min \{ \chi(G), \chi(H) \} $ . Let's define $ P(n) $ to be the proposition that $ \chi(G \times H) \ge n $ whenever $ \chi(G) \ge n $ and $ \chi(H) \ge n $ . Then the above conjecture is equivalent to the statement that $ P(n) $ holds for every positive integer $ n $ . Now $ P(1) $ holds trivially and $ P(2) $ follows from the observation that the product of two graphs each of which contains an edge is a graph which contains an edge. The next case is quite easy too, if $ \chi(G) \ge 3 $ and $ \chi(H) \ge 3 $ , then both $ G $ and $ H $ contain an odd cycle. Since the product of two odd cycles contains an odd cycle, this shows $ \chi(G \times H) \ge 3 $ . The next case up, $ P(4) $ was proved by El-Zahar and Sauer by way of a beautiful argument. It is open for all higher values. A key tool in the proof of El-Zahar and Sauer is the use of exponential graphs. For any pair of graphs $ G, H $ the exponential graph $ G^H $ is a graph whose vertex set consists of all mappings $ f: V(H) \rightarrow V(G) $ . Two vertices $ f,g $ are adjacent if $ f(x)g(y) $ is an edge of $ G $ whenever $ xy $ is an edge of $ H $ . It is easy to see the relevance of $ K_n^G $ to this problem. If we have an $ n $ -coloring $ f $ of $ G \times H $ , then for every vertex $ x \in V(H) $ , there is a mapping $ f_x : V(G) \rightarrow V(K_n) $ given by $ f_x(v) = f(v,x) $ . This associates each $ x \in V(H) $ with a vertex in $ K_n^G $ . Now it is easy to verify that whenever $ x,y $ are adjacent vertices in $ H $ , the maps $ f_x $ and $ f_y $ are adjacent in $ K_n^G $ . Rather more surprisingly, Hedetniemi's conjecture may be reformulated as follows: Conjecture (version 2 of Hedetniemi) If $ \chi(G) > n $ , then $ K_n^G $ is $ n $ -colorable. The following conjecture asserts that Hedetniemi's conjecture still holds with circular chromatic number instead of the usual chromatic number. Here $ \chi_c(G) $ is the circular chromatic number of $ G $ . Since $ \chi(G) = \lceil \chi_c(G) \rceil $ this is a generalization of the original conjecture. Conjecture (Zhu) If $ G $ and $ H $ are finite simple graphs then $ \chi_c(G \times H) = \min\{ \chi_c(G), \chi_c(H) \} $ . A graph $ G $ has circular chromatic number $ \frac{n}{k} $ for positive integers $ n,k $ if and only if $ G $ has a homomorphism to the graph $ K_{n/k} $ . This is a graph whose vertex set consists of $ n $ vertices cyclically ordered, with two vertices adjacent if they are distance $ \ge k $ apart in the cyclic ordering. So again, we may state this conjecture in terms of homomorphisms to graphs of the form $ K_{n/k} $ . More generally, let us call a graph $ K $ multiplicative if $ G \times H \rightarrow K $ implies either $ G \rightarrow K $ or $ H \rightarrow K $ . Now Hedetniemi's conjecture asserts that every $ K_n $ is multiplicative and Zhu's conjecture asserts that every $ K_{n/k} $ is multiplicative. With this terminology, El-Zahar and Sauer proved that $ K_3 $ is multiplicative. A clever generalization of their argument due to Haggkvist, Hell, Miller and Neumann Lara showed that every odd cycle is multiplicative. Recently, Tardif bootstrapped this theorem with the help of a couple of interesting operators on the category of graphs to prove the $ K_{n/k} $ is multiplicative whenever $ n/k < 4 $ . Ignoring trivial cases and equivalences, these are essentially the only graphs known to be multiplicative. It might be tempting to hope that all graphs are multiplicative, but this is false. To construct a non-multiplicative graph, take two graphs $ G,H $ with the property that $ G \not\rightarrow H $ and $ H \not\rightarrow G $ (for instance $ K_3 $ and the Grotzsch Graph). Now $ G \times H $ is not multiplicative since $ G \not\rightarrow G \times H $ and $ H \not\rightarrow G \times H $ , but $ G \times H \rightarrow G \times H $ . It seems that there is no general conjecture as to what graphs are multiplicative. Some other Cayley graphs look like reasonable candidates to me (M. DeVos), but I haven't any evidence one way or the other. Poljak and Rodl defined the function $ f(n) = \min \{ \chi(G \times H) : \chi(G) = n = \chi(H) \} $ . So, Hedetniemi's conjecture is equivalent to $ f(n) = n $ . Using an interesing inequality relating the chromatic number of a digraph $ D $ to the chromatic number of a type of line graph of $ D $ , they were able to prove the following quite surprising result: Either $ f $ is bounded by $ 9 $ or $ \lim_{n \rightarrow \infty} f(n) = \infty $ . There are a number of interesting partial results not mentioned here, and the reader is encouraged to see the survey article by Zhu.

=== Catalog page (statement + literature review) ===
Hedetniemi's Conjecture — Graph-theory open problems

 
 Status
 disproved
 high confidence
 

 Hedetniemi's 1966 conjecture — that $\chi(G \times H) = \min(\chi(G), \chi(H))$ for the tensor product — was disproved by Shitov in 2019 via finite simple graphs $G,H$ with $\chi(G \times H) < \min(\chi(G), \chi(H))$. Subsequent work produced increasingly smaller counterexamples: Zhu gave explicit counterexamples with chromatic number 225, Tardif and others brought the colourability threshold down to $c=14$ and $c=13$, and Wrochna reduced it further to $c=5$. In the $c$-colourability formulation, the conjecture is now known to fail for $c \ge 4$ and to hold for $c \le 3$.

 Cited literature (3)

 
 
 
counterexample Counterexamples to Hedetniemi's conjecture
 (2019)
 

 
 Yaroslav Shitov · Annals of Mathematics · arXiv:1905.02167 · doi:10.4007/annals.2019.190.2.6

Constructs finite simple graphs $G, H$ with $\chi(G \times H) < \min(\chi(G), \chi(H))$, refuting the conjecture in general.
 

 
 
counterexample Relatively small counterexamples to Hedetniemi's conjecture
 (2021)
 

 
 Xuding Zhu · Journal of Combinatorial Theory, Series B · arXiv:2004.09028 · doi:10.1016/j.jctb.2020.09.005

Improves Shitov's refutation by constructing counterexamples with chromatic number 225 (graphs of 10,952 and 33,377 vertices).
 

 
 
counterexample Smaller counterexamples to Hedetniemi's conjecture
 (2020)
 

 
 Marcin Wrochna · arXiv preprint (math.CO) · arXiv:2012.13558

Pushes the smallest known counterexample down to $c = 5$ via wide colourings and lexicographic products (graphs of 4686 and 30 vertices).
 

 

 Reviewer notes. The Annals page directly verifies Shitov's title, author, pages 663-667 in volume 190, and DOI 10.4007/annals.2019.190.2.6. Zhu's arXiv page verifies the explicit chromatic-number-225 counterexamples, and the ScienceDirect page verifies the JCTB 2021 publication and DOI. The statement about failure for all $c\ge4$ in the $c$-colourability formulation is supported by the 2025 survey search result; it is included only in the summary, not as a primary counterexample citation.

 
 Auto-reviewed 2026-05-08 with claude (main agent, web search + fetch) (web search enabled).
 

Conjecture. If $ G,H $ are simple finite graphs, then $ \chi(G \times H) = \min \{ \chi(G), \chi(H) \} $ .

Keywords:
categorical product · coloring · homomorphism · tensor product

Discussion

This beautiful and seemingly innocent conjecture asserts a deep and important property of graph coloring. It is undoubtedly one of the most significant unsolved problems in graph coloring and graph homomorphisms. We write $ G \rightarrow H $ if there is a homomorphism from $ G $ to $ H $ . The graph $ G \times H $ has a two natural projection maps (projecting onto either the first or second coordinate), and these maps are homomorphisms to $ G $ and to $ H $ . So, in short, $ G \times H \rightarrow G $ and $ G \times H \rightarrow H $ . A graph is $ n $ -colorable if and only if it has a homomorphism to $ K_n $ . Combining this with the transitivity of $ \rightarrow $ we find that $ \chi(G \times H) \le \min\{ \chi(G), \chi(H) \} $ (indeed, if $ \chi(G) = n $ , then $ G \times H \rightarrow G $ and $ G \rightarrow K_n $ , so $ G \times H \rightarrow K_n $ - equivalently, $ G \times H $ is $ n $ -colorable). So, the hard direction of Hedetniemi's Conjecture is to prove that $ \chi(G \times H) \ge \min \{ \chi(G), \chi(H) \} $ . Let's define $ P(n) $ to be the proposition that $ \chi(G \times H) \ge n $ whenever $ \chi(G) \ge n $ and $ \chi(H) \ge n $ . Then the above conjecture is equivalent to the statement that $ P(n) $ holds for every positive integer $ n $ . Now $ P(1) $ holds trivially and $ P(2) $ follows from the observation that the product of two graphs each of which contains an edge is a graph which contains an edge. The next case is quite easy too, if $ \chi(G) \ge 3 $ and $ \chi(H) \ge 3 $ , then both $ G $ and $ H $ contain an odd cycle. Since the product of two odd cycles contains an odd cycle, this shows $ \chi(G \times H) \ge 3 $ . The next case up, $ P(4) $ was proved by El-Zahar and Sauer by way of a beautiful argument. It is open for all higher values. A key tool in the proof of El-Zahar and Sauer is the use of exponential graphs. For any pair of graphs $ G, H $ the exponential graph $ G^H $ is a graph whose vertex set consists of all mappings $ f: V(H) \rightarrow V(G) $ . Two vertices $ f,g $ are adjacent if $ f(x)g(y) $ is an edge of $ G $ whenever $ xy $ is an edge of $ H $ . It is easy to see the relevance of $ K_n^G $ to this problem. If we have an $ n $ -coloring $ f $ of $ G \times H $ , then for every vertex $ x \in V(H) $ , there is a mapping $ f_x : V(G) \rightarrow V(K_n) $ given by $ f_x(v) = f(v,x) $ . This associates each $ x \in V(H) $ with a vertex in $ K_n^G $ . Now it is easy to verify that whenever $ x,y $ are adjacent vertices in $ H $ , the maps $ f_x $ and $ f_y $ are adjacent in $ K_n^G $ . Rather more surprisingly, Hedetniemi's conjecture may be reformulated as follows: Conjecture (version 2 of Hedetniemi) If $ \chi(G) > n $ , then $ K_n^G $ is $ n $ -colorable. The following conjecture asserts that Hedetniemi's conjecture still holds with circular chromatic number instead of the usual chromatic number. Here $ \chi_c(G) $ is the circular chromatic number of $ G $ . Since $ \chi(G) = \lceil \chi_c(G) \rceil $ this is a generalization of the original conjecture. Conjecture (Zhu) If $ G $ and $ H $ are finite simple graphs then $ \chi_c(G \times H) = \min\{ \chi_c(G), \chi_c(H) \} $ . A graph $ G $ has circular chromatic number $ \frac{n}{k} $ for positive integers $ n,k $ if and only if $ G $ has a homomorphism to the graph $ K_{n/k} $ . This is a graph whose vertex set consists of $ n $ vertices cyclically ordered, with two vertices adjacent if they are distance $ \ge k $ apart in the cyclic ordering. So again, we may state this conjecture in terms of homomorphisms to graphs of the form $ K_{n/k} $ . More generally, let us call a graph $ K $ multiplicative if $ G \times H \rightarrow K $ implies either $ G \rightarrow K $ or $ H \rightarrow K $ . Now Hedetniemi's conjecture asserts that every $ K_n $ is multiplicative and Zhu's conjecture asserts that every $ K_{n/k} $ is multiplicative. With this terminology, El-Zahar and Sauer proved that $ K_3 $ is multiplicative. A clever generalization of their argument due to Haggkvist, Hell, Miller and Neumann Lara showed that every odd cycle is multiplicative. Recently, Tardif bootstrapped this theorem with the help of a couple of interesting operators on the category of graphs to prove the $ K_{n/k} $ is multiplicative whenever $ n/k < 4 $ . Ignoring trivial cases and equivalences, these are essentially the only graphs known to be multiplicative. It might be tempting to hope that all graphs are multiplicative, but this is false. To construct a non-multiplicative graph, take two graphs $ G,H $ with the property that $ G \not\rightarrow H $ and $ H \not\rightarrow G $ (for instance $ K_3 $ and the Grotzsch Graph). Now $ G \times H $ is not multiplicative since $ G \not\rightarrow G \times H $ and $ H \not\rightarrow G \times H $ , but $ G \times H \rightarrow G \times H $ . It seems that there is no general conjecture as to what graphs are multiplicative. Some other Cayley graphs look like reasonable candidates to me (M. DeVos), but I haven't any evidence one way or the other. Poljak and Rodl defined the function $ f(n) = \min \{ \chi(G \times H) : \chi(G) = n = \chi(H) \} $ . So, Hedetniemi's conjecture is equivalent to $ f(n) = n $ . Using an interesing inequality relating the chromatic number of a digraph $ D $ to the chromatic number of a type of line graph of $ D $ , they were able to prove the following quite surprising result: Either $ f $ is bounded by $ 9 $ or $ \lim_{n \rightarrow \infty} f(n) = \infty $ . There are a number of interesting partial results not mentioned here, and the reader is encouraged to see the survey article by Zhu.
