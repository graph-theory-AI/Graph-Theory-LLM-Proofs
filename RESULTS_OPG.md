# Results

Auto-generated from `attacks_opg/*/verdict.json` by `python attack.py summary`.
**These are unrefereed model self-reports.** A `proved` / `disproved` label is
not a theorem. `would_publish` is the model's own claim that it would submit
the writeup to a journal.

Catalog: [mlelarge/graph-conjectures](https://graph-theory-ai.github.io/graph-conjectures).
Model: `gpt-6-astra`, reasoning effort `max`, `mode=pro`. Ultra / 64-subagent
runs were not used.

## Counts

Finished attacks with a verdict: **227**.
Spend (promo ledger × prepaid FX): **€241.22** billed USD
**$232.89** / budget €600
(safety margin €5).

| verdict | n | would_publish |
| --- | ---: | ---: |
| proved | 6 | 5 |
| disproved | 15 | 4 |
| already_resolved | 29 | 0 |
| partial | 177 | 1 |

## Claimed proofs (6)

| id | conf. | publish? | one line |
| --- | --- | --- | --- |
| [`asymptotic_distribution_of_form_of_polyhedra`](https://graph-theory-ai.github.io/graph-conjectures/op/asymptotic_distribution_of_form_of_polyhedra/) · [artifact](attacks_opg/asymptotic_distribution_of_form_of_polyhedra/) | high | no | For a uniformly chosen unlabelled polyhedral graph with k edges, β converges to 1/2 and √k(β−1/2) converges to a normal law of variance 1/32. |
| [`chromatic_number_of_random_lifts_of_complete_graphs`](https://graph-theory-ai.github.io/graph-conjectures/op/chromatic_number_of_random_lifts_of_complete_graphs/) · [artifact](attacks_opg/chromatic_number_of_random_lifts_of_complete_graphs/) | high | yes | A random h-lift of K_5 has chromatic number 3 asymptotically almost surely. |
| [`finding_k_edge_outerplanar_graph_embeddings`](https://graph-theory-ai.github.io/graph-conjectures/op/finding_k_edge_outerplanar_graph_embeddings/) · [artifact](attacks_opg/finding_k_edge_outerplanar_graph_embeddings/) | high | yes | A polynomial-time SPQR dynamic program, using a two-bin scheduling recurrence at parallel nodes, computes a minimum edge-outerplanar embedding. |
| [`imbalance_conjecture`](https://graph-theory-ai.github.io/graph-conjectures/op/imbalance_conjecture/) · [artifact](attacks_opg/imbalance_conjecture/) | high | yes | A truncated-tail inequality for edge imbalances implies every Erdős–Gallai inequality and proves the conjecture. |
| [`mixing_circular_colourings_0`](https://graph-theory-ai.github.io/graph-conjectures/op/mixing_circular_colourings_0/) · [artifact](attacks_opg/mixing_circular_colourings_0/) | high | yes | For an n-vertex graph with an edge, the circular mixing threshold is rational, with reduced numerator at most n+1. |
| [`three_chromatic_0_2_graphs`](https://graph-theory-ai.github.io/graph-conjectures/op/three_chromatic_0_2_graphs/) · [artifact](attacks_opg/three_chromatic_0_2_graphs/) | high | yes | Every finite 3-colourable (0,2)-graph is bipartite, so none has chromatic number exactly three. |

## Claimed counterexamples (15)

| id | conf. | publish? | one line |
| --- | --- | --- | --- |
| [`a_generalization_of_vizings_theorem`](https://graph-theory-ai.github.io/graph-conjectures/op/a_generalization_of_vizings_theorem/) · [artifact](attacks_opg/a_generalization_of_vizings_theorem/) | high | yes | A probabilistic construction gives a simple 100-uniform hypergraph with maximum 99-codegree at most 200 that requires at least 451 colors, contradicting the proposed bound of 299. |
| [`are_critical_k_forests_tight`](https://graph-theory-ai.github.io/graph-conjectures/op/are_critical_k_forests_tight/) · [artifact](attacks_opg/are_critical_k_forests_tight/) | high | no | An explicit six-vertex, nine-edge 3-forest is inclusion-maximal but not tight. |
| [`bene_conjecture_graph_theoretic_form_0`](https://graph-theory-ai.github.io/graph-conjectures/op/bene_conjecture_graph_theoretic_form_0/) · [artifact](attacks_opg/bene_conjecture_graph_theoretic_form_0/) | high | no | An explicit simple cubic ordered two-stage graph has F(L)=3 but R(L)≥9, contradicting R(L)≤2F(L). |
| [`cores_of_cayley_graphs`](https://graph-theory-ai.github.io/graph-conjectures/op/cores_of_cayley_graphs/) · [artifact](attacks_opg/cores_of_cayley_graphs/) | high | no | For M = Z/4Z, the Cayley graph C4 has core K2, which cannot be a Cayley graph on any direct power of M. |
| [`covering_powers_of_cycles_with_equivalence_subgraphs`](https://graph-theory-ai.github.io/graph-conjectures/op/covering_powers_of_cycles_with_equivalence_subgraphs/) · [artifact](attacks_opg/covering_powers_of_cycles_with_equivalence_subgraphs/) | high | yes | Noncomplete powers of cycles have equivalence covering number Θ(log(k+1)), contradicting the proposed Ω(k) lower bound. |
| [`cyclic_spanning_subdigraph_with_small_cyclomatic_number`](https://graph-theory-ai.github.io/graph-conjectures/op/cyclic_spanning_subdigraph_with_small_cyclomatic_number/) · [artifact](attacks_opg/cyclic_spanning_subdigraph_with_small_cyclomatic_number/) | high | no | As formulated for possibly nonstrong digraphs, the claim has a ten-vertex oriented counterexample with stability number 2 and minimum cyclic-spanning cyclomatic number 3. |
| [`geodesic_cycles_and_tuttes_theorem`](https://graph-theory-ai.github.io/graph-conjectures/op/geodesic_cycles_and_tuttes_theorem/) · [artifact](attacks_opg/geodesic_cycles_and_tuttes_theorem/) | high | yes | The eight-vertex graph obtained by inserting a degree-three vertex into every face of a tetrahedron is a counterexample. |
| [`hamilton_cycle_in_small_d_diregular_graphs`](https://graph-theory-ai.github.io/graph-conjectures/op/hamilton_cycle_in_small_d_diregular_graphs/) · [artifact](attacks_opg/hamilton_cycle_in_small_d_diregular_graphs/) | high | no | Under the stated minimum-degree definition, two regular tournaments sharing one vertex give a counterexample on exactly 4d+1 vertices. |
| [`large_acyclic_induced_subdigraph_in_a_planar_oriented_graph`](https://graph-theory-ai.github.io/graph-conjectures/op/large_acyclic_induced_subdigraph_in_a_planar_oriented_graph/) · [artifact](attacks_opg/large_acyclic_induced_subdigraph_in_a_planar_oriented_graph/) | high | no | An explicit seven-vertex planar oriented graph has maximum acyclic induced order four, and an infinite family has acyclic fraction tending to one half. |
| [`matching_cut_and_girth`](https://graph-theory-ai.github.io/graph-conjectures/op/matching_cut_and_girth/) · [artifact](attacks_opg/matching_cut_and_girth/) | high | no | For every girth bound there is a simple 7-regular graph with no matching cut, so d = 8 refutes the universal assertion. |
| [`melnikovs_valency_variety_problem`](https://graph-theory-ai.github.io/graph-conjectures/op/melnikovs_valency_variety_problem/) · [artifact](attacks_opg/melnikovs_valency_variety_problem/) | high | yes | A 37-vertex graph has chromatic number 3 and degree set {0,1,...,29}, making the proposed right-hand side equal to 3; moreover, 37 vertices is minimum. |
| [`odd_cycles_and_low_oddness`](https://graph-theory-ai.github.io/graph-conjectures/op/odd_cycles_and_low_oddness/) · [artifact](attacks_opg/odd_cycles_and_low_oddness/) | high | no | A connected simple bridgeless cubic graph on 30 vertices has every 2-factor of type 5+5+5+15, and therefore has oddness 4. |
| [`strong_matchings_and_covers`](https://graph-theory-ai.github.io/graph-conjectures/op/strong_matchings_and_covers/) · [artifact](attacks_opg/strong_matchings_and_covers/) | high | no | With the stated vertex-cover definition, the conjecture is false already for a countable complete multipartite graph with part sizes 1, 2, 3, ... . |
| [`turan_number_of_a_finite_family`](https://graph-theory-ai.github.io/graph-conjectures/op/turan_number_of_a_finite_family/) · [artifact](attacks_opg/turan_number_of_a_finite_family/) | high | no | As written, the conjecture fails for the family {P3, 2K2}: its Turán number is 1, while both individual Turán numbers grow linearly. |
| [`what_is_the_smallest_number_of_disjoint_spanning_trees_made_a_graph_hamiltonian`](https://graph-theory-ai.github.io/graph-conjectures/op/what_is_the_smallest_number_of_disjoint_spanning_trees_made_a_graph_hamiltonian/) · [artifact](attacks_opg/what_is_the_smallest_number_of_disjoint_spanning_trees_made_a_graph_hamiltonian/) | high | no | Under the stated deletion procedure, the requested minimum need not exist, even with metric weights and uniquely determined minimum trees. |

## Already resolved (model says the literature already closed it) (29)

| id | conf. | publish? | one line |
| --- | --- | --- | --- |
| [`antichains_in_the_cycle_continuous_order`](https://graph-theory-ai.github.io/graph-conjectures/op/antichains_in_the_cycle_continuous_order/) · [artifact](attacks_opg/antichains_in_the_cycle_continuous_order/) | high | no | The supplied catalog records Šámal’s affirmative solution, strengthened to an embedding of every countable poset into the cycle-continuous quasi-order. |
| [`book_thickness_of_subdivisions`](https://graph-theory-ai.github.io/graph-conjectures/op/book_thickness_of_subdivisions/) · [artifact](attacks_opg/book_thickness_of_subdivisions/) | high | no | The conjecture is false even for exact one-subdivisions: graphs of unbounded book thickness can have one-subdivisions of book thickness at most 5. |
| [`bounding_the_on_line_choice_number_in_terms_of_the_choice_number`](https://graph-theory-ai.github.io/graph-conjectures/op/bounding_the_on_line_choice_number_in_terms_of_the_choice_number/) · [artifact](attacks_opg/bounding_the_on_line_choice_number_in_terms_of_the_choice_number/) | high | no | Duraj, Gutowski, and Kozik resolved the question affirmatively: the online-minus-offline choice-number gap for K_{N,N} is of order log log N. |
| [`chromatic_number_of_common_graphs`](https://graph-theory-ai.github.io/graph-conjectures/op/chromatic_number_of_common_graphs/) · [artifact](attacks_opg/chromatic_number_of_common_graphs/) | high | no | No: Kráľ, Volec, and Wei proved that connected common graphs exist with every prescribed positive chromatic number. |
| [`circular_flow_number_of_regular_class_1_graphs`](https://graph-theory-ai.github.io/graph-conjectures/op/circular_flow_number_of_regular_class_1_graphs/) · [artifact](attacks_opg/circular_flow_number_of_regular_class_1_graphs/) | high | no | The supplied literature record reports a disproof, with counterexamples already for t=6. |
| [`circular_flow_numbers_of_r_graphs`](https://graph-theory-ai.github.io/graph-conjectures/op/circular_flow_numbers_of_r_graphs/) · [artifact](attacks_opg/circular_flow_numbers_of_r_graphs/) | high | no | The class-1 counterexample theorem reported in the supplied catalog already disproves the stated r-graph conjecture, including at t=6. |
| [`coloring_the_odd_distance_graph`](https://graph-theory-ai.github.io/graph-conjectures/op/coloring_the_odd_distance_graph/) · [artifact](attacks_opg/coloring_the_odd_distance_graph/) | high | no | Davies's published theorem excludes every finite coloring of the odd-distance graph; in fact, its chromatic number is exactly countably infinite. |
| [`cores_of_strongly_regular_graphs`](https://graph-theory-ai.github.io/graph-conjectures/op/cores_of_strongly_regular_graphs/) · [artifact](attacks_opg/cores_of_strongly_regular_graphs/) | high | no | Yes: the primitive case satisfies the stronger isomorphism-or-clique-image dichotomy, and the imprimitive cases have complete cores. |
| [`edge_disjoint_hamilton_cycles`](https://graph-theory-ai.github.io/graph-conjectures/op/edge_disjoint_hamilton_cycles/) · [artifact](attacks_opg/edge_disjoint_hamilton_cycles/) | high | no | Thomassen's conjecture is a published theorem, with the optimal-order connectivity bound f(k)=O(k^2). |
| [`end_devouring_rays`](https://graph-theory-ai.github.io/graph-conjectures/op/end_devouring_rays/) · [artifact](attacks_opg/end_devouring_rays/) | high | no | The supplied catalog records the resolution, and a minimum-distance prefix construction gives a self-contained proof. |
| [`erdos_posa_property_for_long_directed_cycles`](https://graph-theory-ai.github.io/graph-conjectures/op/erdos_posa_property_for_long_directed_cycles/) · [artifact](attacks_opg/erdos_posa_property_for_long_directed_cycles/) | high | no | The directed grid theorem resolves the conjecture, via a packing–transversal lemma for digraphs of bounded directed treewidth. |
| [`every_prism_over_a_3_connected_planar_graph_is_hamiltonian`](https://graph-theory-ai.github.io/graph-conjectures/op/every_prism_over_a_3_connected_planar_graph_is_hamiltonian/) · [artifact](attacks_opg/every_prism_over_a_3_connected_planar_graph_is_hamiltonian/) | high | no | The conjecture is false: the supplied literature record identifies Špacapan’s published construction of a 3-connected planar graph with a non-Hamiltonian prism. |
| [`extremal_problem_on_the_number_of_tree_endomorphism`](https://graph-theory-ai.github.io/graph-conjectures/op/extremal_problem_on_the_number_of_tree_endomorphism/) · [artifact](attacks_opg/extremal_problem_on_the_number_of_tree_endomorphism/) | high | no | The conjecture is exactly the Csikvári–Lin theorem identified in the supplied literature review. |
| [`forcing_a_2_regular_minor`](https://graph-theory-ai.github.io/graph-conjectures/op/forcing_a_2_regular_minor/) · [artifact](attacks_opg/forcing_a_2_regular_minor/) | high | no | The stated conjecture was proved by Csóka, Lo, Norin, Wu, and Yepremyan in their 2017 paper, The extremal function for disconnected minors. |
| [`goldbergs_conjecture`](https://graph-theory-ai.github.io/graph-conjectures/op/goldbergs_conjecture/) · [artifact](attacks_opg/goldbergs_conjecture/) | high | no | The stated inequality is the established Goldberg–Seymour theorem; the original OpenProblemGarden discussion is outdated. |
| [`grunbaums_conjecture`](https://graph-theory-ai.github.io/graph-conjectures/op/grunbaums_conjecture/) · [artifact](attacks_opg/grunbaums_conjecture/) | high | no | The full conjecture was disproved by Kochol (2009), using snarks with polyhedral embeddings in orientable surfaces. |
| [`hedetniemis_conjecture`](https://graph-theory-ai.github.io/graph-conjectures/op/hedetniemis_conjecture/) · [artifact](attacks_opg/hedetniemis_conjecture/) | high | no | Hedetniemi’s conjecture was disproved by Shitov in 2019; below is a self-contained, nonoptimized counterexample construction. |
| [`highly_arc_transitive_two_ended_digraphs`](https://graph-theory-ai.github.io/graph-conjectures/op/highly_arc_transitive_two_ended_digraphs/) · [artifact](attacks_opg/highly_arc_transitive_two_ended_digraphs/) | high | no | The conjecture is false: an explicit two-ended highly arc-transitive digraph has connected, noncomplete bipartite tiles. |
| [`jaegers_modular_orientation_conjecture`](https://graph-theory-ai.github.io/graph-conjectures/op/jaegers_modular_orientation_conjecture/) · [artifact](attacks_opg/jaegers_modular_orientation_conjecture/) | medium | no | The supplied catalog reports a prior disproof for every k≥3, and the circular-flow counterexamples apply to exactly the stated modular-orientation conjecture. |
| [`laplacian_degrees_of_a_graph`](https://graph-theory-ai.github.io/graph-conjectures/op/laplacian_degrees_of_a_graph/) · [artifact](attacks_opg/laplacian_degrees_of_a_graph/) | high | no | The conjecture is true in full, as the supplied catalog reports, and a self-contained proof is given below. |
| [`number_of_cliques_in_minor_closed_classes`](https://graph-theory-ai.github.io/graph-conjectures/op/number_of_cliques_in_minor_closed_classes/) · [artifact](attacks_opg/number_of_cliques_in_minor_closed_classes/) | high | no | The original question is settled affirmatively by the published Fox–Wei bound of 3^{2t/3+o(t)} n cliques. |
| [`partitionning_a_tournament_into_k_strongly_connected_subtournaments`](https://graph-theory-ai.github.io/graph-conjectures/op/partitionning_a_tournament_into_k_strongly_connected_subtournaments/) · [artifact](attacks_opg/partitionning_a_tournament_into_k_strongly_connected_subtournaments/) | high | no | The established uniform partition theorem gives an affirmative answer, with g(k_1,...,k_p) <= C p max_i k_i for an absolute constant C. |
| [`ptas_for_feedback_arc_set_in_tournaments`](https://graph-theory-ai.github.io/graph-conjectures/op/ptas_for_feedback_arc_set_in_tournaments/) · [artifact](attacks_opg/ptas_for_feedback_arc_set_in_tournaments/) | high | no | Yes: Kenyon-Mathieu and Schudy established a PTAS for feedback arc set in tournaments at STOC 2007. |
| [`real_roots_of_the_flow_polynomial`](https://graph-theory-ai.github.io/graph-conjectures/op/real_roots_of_the_flow_polynomial/) · [artifact](attacks_opg/real_roots_of_the_flow_polynomial/) | high | no | The conjecture is false: the published counterexample G(119,7) has a nonzero flow polynomial with real roots greater than 5. |
| [`seymours_r_graph_conjecture`](https://graph-theory-ai.github.io/graph-conjectures/op/seymours_r_graph_conjecture/) · [artifact](attacks_opg/seymours_r_graph_conjecture/) | high | no | Seymour’s r-graph conjecture is an immediate corollary of the proved Goldberg–Seymour edge-colouring theorem. |
| [`universal_highly_arc_transitive_digraphs`](https://graph-theory-ai.github.io/graph-conjectures/op/universal_highly_arc_transitive_digraphs/) · [artifact](attacks_opg/universal_highly_arc_transitive_digraphs/) | high | no | Yes: an explicit construction from a biregular tree gives universal highly arc-transitive digraphs of every composite common indegree and outdegree. |
| [`vertex_coloring_of_graph_fractional_powers`](https://graph-theory-ai.github.io/graph-conjectures/op/vertex_coloring_of_graph_fractional_powers/) · [artifact](attacks_opg/vertex_coloring_of_graph_fractional_powers/) | high | no | The triangular prism P is an explicit counterexample: χ(P^{3/5}) = 6 while ω(P^{3/5}) = 5. |
| [`vertex_minor_closed_classes_are_chi_bounded`](https://graph-theory-ai.github.io/graph-conjectures/op/vertex_minor_closed_classes_are_chi_bounded/) · [artifact](attacks_opg/vertex_minor_closed_classes_are_chi_bounded/) | high | no | Yes: James Davies proved that every proper vertex-minor-closed class of finite simple graphs is chi-bounded. |
| [`what_is_the_largest_graph_of_positive_curvature`](https://graph-theory-ai.github.io/graph-conjectures/op/what_is_the_largest_graph_of_positive_curvature/) · [artifact](attacks_opg/what_is_the_largest_graph_of_positive_curvature/) | high | no | The exact maximum is 208 vertices: Ghidelli proved the upper bound, and an explicit attaining construction is verified below. |

## Ill-posed / no determinate statement as supplied (0)

| id | conf. | publish? | one line |
| --- | --- | --- | --- |

## Coverage

The sweep queue is the easiest-first open/partial arXiv ranking (227
records, including a handful of questions restored after catalog extraction
fixes). Open Problem Garden entries were **not** attacked.

Queue records not yet attacked: **0** (plus 0 skipped without a model call).

Generated 2026-09-16T20:27:59Z.
