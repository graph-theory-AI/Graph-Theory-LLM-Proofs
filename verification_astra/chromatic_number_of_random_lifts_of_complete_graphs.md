---
id: chromatic_number_of_random_lifts_of_complete_graphs
leg: attacks_opg
claimed_verdict: proved
review_verdict: MINOR_GAPS
confidence: medium
interpretation_ok: true
references_ok: true
computation_run: true
one_line: The load-bearing novelty — a Bregman/permanent bound that keeps the perfect-matching constraint Nir–Pérez-Giménez relaxed away, making the uniform overlap the global second-moment maximum at d=4 — survives full re-derivation and numerical attack, so the a.a.s. 3-colourability of random lifts of K_5 appears genuinely proved; only two standard-but-sketched analytic steps (the uniform local CLT of Lemma 2 and the small-subgraph-conditioning limit in §7) fall short of being written out.
---

## Interpretation

The OPG entry (attributed to Amit, Linial, Matoušek [ALM02]) asks: *is the chromatic
number of a random lift of K_5 concentrated on a single value?* The discussion fixes
the model (uniform random h-lift = independent uniform perfect matching per base edge,
h → ∞) and records that the value is 3 or 4.

The writeup proves Pr(χ(H_n) = 3) → 1 for H_n a random n-lift of K_5, using exactly
that model (Section 1: "for each uv ∈ E, a uniform perfect matching between the
fibres", independent across the 10 edges of K_5). "Asymptotically almost surely" is in
n = h, the lift order, with the base K_5 fixed — the intended asymptotics. The
writeup separately excludes χ = 2 (Section 8), so it really delivers a single value,
not just an upper bound. This is the intended question, answered affirmatively with
the value identified; a reasonable author of the original problem would consider the
K_5 question resolved.

Two scope points, neither an interpretation game:

* The OPG entry also asks the general question for K_n. The writeup does not address
  it (its "Scope" section only extends the *upper* bound χ ≤ 3 to arbitrary fixed
  simple 4-regular bases). The verdict block does not claim otherwise.
* The writeup works with **fibre-balanced** ("strongly equitable") colourings, i.e.
  each fibre gets t_a ∈ {⌊n/3⌋, ⌈n/3⌉} vertices of colour a. That is a legitimate
  restriction: Z_n > 0 implies 3-colourability. It is the same object NPG call Y.

## Step-by-step findings

I re-derived every formula independently; "re-derived" below means I obtained the
same expression from scratch, not that I read the writeup's derivation.

| step | label | note |
|---|---|---|
| 1. (1) E Z_n = M_n^5 a_n^{10} | VALID | Matchings independent across the 10 base edges; a_n depends only on the fibre colour counts, which are the same t for every fibre, so it is the same for all 10 edges and all fibre-balanced colourings. |
| 2. (2) Pr(ρ_i = ρ) = Π_a(t_a!)² / (n! Π_{ab}(nρ_ab)!) | VALID | Re-derived: #{colourings 2 with overlap ρ} = Π_a t_a!/Π_b(nρ_ab)!, divided by n!/Π t_a!. |
| 3. (3) E Z_n²/(E Z_n)² = E_ρ Π_{ij∈E} q_n(ρ_i,ρ_j)/a_n² | VALID | Conditional on the two colourings, the 10 matchings are independent, and the pair-properness probability for edge ij depends only on (ρ_i, ρ_j). |
| 4. Reduction F(ρ) = −log3 + (1/3)Σ g(3ρ_ab), g(x)=2x log(1+x) − x log x | VALID | Re-derived exactly: H(ρ) = −(1/3)Σ x log x + log 3, L(ρ) = (1/3)Σ x log(1+x) − log 3 with x = 3ρ. F(U)=2log(4/3) confirmed. |
| 5. g''(x) = (x²+2x−1)/(x(1+x)²), sign change at √2−1 | VALID | Re-derived; matches numerics to 1e−6 (script 01). |
| 6. Lemma 1, case "all coordinates ≤ r": Jensen | VALID | g concave on [0,r], r = √2−1 > 1/3, so Σg(x_i) ≤ 3g(1/3). |
| 7. Lemma 1, "no interior maximizer has two coordinates > r" | VALID | Moving two convex-region coordinates with fixed sum has positive second derivative, so such a point is a local minimum in that direction. g'(0+) = +∞ rules out boundary maximizers. |
| 8. Lemma 1, one-coordinate case: φ(x) = g(x) + 2g((1−x)/2) | VALID | The other two coordinates are ≤ r and their mean (1−x)/2 ≤ (1−r)/2 < r, so concavity applies. |
| 9. φ'' numerator N(x) = x⁴ − 10x³ − 32x² + 34x − 9 | VALID | I expanded (x²+2x−1)(1−x)(3−x)² + (x²−6x+1)x(1+x)² by hand and got exactly this polynomial. |
| 10. N(x) ≤ −(103/3)x² + 34x − 9 on [1/3,1), discriminant −80 | VALID | The bound is equivalent to x² − 10x + 7/3 ≤ 0, true for x ≥ 0.2390; 34² − 4·(103/3)·9 = 1156 − 1236 = −80. Numerically max N on [1/3,1) = −1.0488. |
| 11. Lemma 1 conclusion + Hessian −(9/8)I at U, quadratic gap (4) | VALID | 3g''(1/3) = −9/8 confirmed. Compactness + uniqueness ⇒ (4). Numerically the max of Σg over the simplex is attained only at (1/3,1/3,1/3) for d = 4 (script 01c). |
| 12. (6) uniform version for rounded row sums p | GAP (routine) | The continuity-of-entropy estimate ("changes the matrix by O(1/n) in total variation, entropy by O(log n / n)") is asserted, not proved; it is the standard Fannes-type bound and the O(log n) it produces is swamped by exp(−c n^{1/5}). |
| 13. (7) Bregman/Minc: per(A) ≤ Π_v (r_v!)^{1/r_v} | VALID | Correctly stated theorem (Bregman 1973; entropy proof Radhakrishnan 1997); the writeup's sketch is Radhakrishnan's argument. |
| 14. Row sums r_v = n(1 − p_a − p_b + σ(a,b)) ≥ n/4 | VALID | Inclusion–exclusion over the two colour classes; 1 − 2/3 + σ ≥ 1/3 − O(1/n). |
| 15. (8) log q_n(ρ,σ) ≤ n Σ ρ_ab log(1/3+σ_ab) + O(log n) | VALID | Re-derived: log(r!)/r = log r − 1 + O(log r / r), subtract log n! = n log n − n + O(log n); the per-row error sums to O(log n) since r_v ≥ n/4. Verified numerically against the exact rate (script 05: max violation −1.4e−5 over 19851 random pairs). |
| 16. (9) symmetrisation | VALID | Σ(ρ−σ)(log(1/3+ρ) − log(1/3+σ)) ≥ 0 termwise since log is increasing. |
| 17. (10) log q_n ≤ (n/2)(L(ρ)+L(σ)) + O(log n) | VALID | Average of (8) and its transpose (per A = per Aᵀ). Numerically confirmed: max of λ(a,b) − (L(a)+L(b))/2 = −1.3e−3 over 19851 pairs. |
| 18. Lemma 2 identity (12): Q = (r/s)^n Pr(S=nβ)/Pr(Mult(n,u)=nβ) | VALID | Re-derived exactly from per(M) = Π(nα_i)! Π(nβ_j)! Σ_m 1/Π m_ij!. |
| 19. Lemma 2 covariance Σ₀ = (1/s)(I − P²) on 1⊥ | VALID | Σ_i u_i[diag(P_{i·}) − P_{i·}P_{i·}ᵀ] = (1/s)(I − P²) using double stochasticity and symmetry of P. |
| 20. Lemma 2 local CLT / Fourier inversion / lattice constant | GAP | This is the one genuinely analytic step and it is a sketch ("Fourier inversion under this tilt gives a Gaussian local prefactor"). The lattice hypothesis is verified correctly (for A₀ and A₁ = A₀⊗A₀ the only maximum-modulus character is trivial), the tilting expansion and the O(δ³) rate-function error are right, and n·O(n^{−6/5}) = o(1) as claimed; but uniformity of the (1+o(1)) is asserted. This is exactly the Greenhill–Janson–Ruciński-type lemma NPG invoke by citation over several pages. Repairable by citation. The formula itself passes a nontrivial internal consistency test: its exponent is symmetric under (α,β) ↔ (β,α), as per(A) = per(Aᵀ) demands. |
| 21. (14) a_n = (4/3)(2/3)^n(1+o(1)) | VALID | det_{1⊥}(I − P₀²)^{−1/2} = (3/4)^{−1} = 4/3 (numerics). Exact a_n computed by inclusion–exclusion for n ≤ 30: ratio a_n / [(4/3)(2/3)^n] = 0.8438, 0.9492, …, 0.9888 → 1. |
| 22. (15) E Z_n = Θ(n^{−5})(4/3)^{5n} | VALID | Exact values for n ≤ 30 give E Z_n / [n^{−5}(4/3)^{5n}] = 4.72, 5.19, 5.49 → the predicted constant (3√3)⁵(4/3)^{10}/(2π)⁵ = 6.87. |
| 23. (16) spec(P₁) = {1, −1/2 (×4), 1/4 (×4)} | VALID | Numerics. |
| 24. (17) log Pr(ρ_i=ρ) = n(H(ρ) − 2H(p)) + O(log n) | VALID | Re-derived by Stirling on (2). |
| 25. (18) contribution ≤ exp{n Σ(F(ρ_i) − F(U))} | VALID | Each fibre lies in 4 base edges, so Σ_{ij∈E}(1/2)(L(ρ_i)+L(ρ_j)) = 2Σ_i L(ρ_i); the normalisation 2log3 + 4log(2/3) equals F(U) exactly. This is where 4-regularity enters, as stated. |
| 26. (19) non-central overlaps contribute o(1) | VALID | n·c'·(n^{−2/5})² = c' n^{1/5}; the number of profiles is O(n^{45}). |
| 27. (20) Pr(ρ_i=ρ) = 729/(2πn)² exp(−‖z‖²/2)(1+o(1)); covolume 729/n² | VALID | Gram matrix of the basis (e_a−e_3)(e_b−e_3)ᵀ is G⊗G with G=[[2,1],[1,2]], det = 3²·3² = 81, covolume 9; the z-lattice then has covolume (3/√n)⁴·9 = 729/n². Independent cross-check: a standard Gaussian on T has entrywise variance [(I−J/3)_{aa}]² = 4/9, and the exact hypergeometric variance of nρ_ab is 4n/81, i.e. Var(3√n ρ_ab) = 4/9. Consistent. Also E ρ_i = C_n exactly. |
| 28. (21) q_n/a_n² = (16/15)² exp{(4/15)⟨z_i,z_j⟩ − (1/30)(‖z_i‖²+‖z_j‖²)}(1+o(1)) | VALID | Re-derived from (11) with s=9, r=4, P₁ = 1/4 on T: prefactor (9/16)·det_{1⊥}(I−P₁²)^{−1/2} = (9/16)(64/45)² = (16/15)² (numerics agree to 1e−15); the exponent reduces to exactly the stated form. |
| 29. (22)–(23) M = (19I₅ − 4A)/15, spec {1/5, 23/15 (×4)} | VALID | Numerics: eig(M) = (0.2, 1.5333×4); positive definite. |
| 30. (24)–(25) R = (16/15)^20 det(M)^{−2} = 25(16/15)^20(15/23)^8 = 2.974554 | VALID | det M = 1.1055447 = (1/5)(23/15)⁴; det(M⊗I₄)^{−1/2} = det(M)^{−2}. |
| 31. (26) μ_ℓ = tr(B^ℓ)/(2ℓ), δ_ℓ = 2(−1/2)^ℓ, Poisson limits | VALID | tr(B³)=60, tr(B⁴)=120, tr(B⁵)=120 ⇒ μ₃=10, μ₄=15, μ₅=12, matching the 10 triangles and 15 four-cycles of K_5 (each base cycle contributes a Poisson(1) fixed-point count). Simulation over 1400 random lifts: mean triangles 9.79–10.20, 4-cycles 14.75–15.15, 5-cycles 11.72–12.13. |
| 32. Size-biased construction (uniform balanced colouring per fibre, then colour-respecting matchings) | VALID | Correct because the properness probability a_n^{10} is the same for every fibre-balanced colouring. |
| 33. (27) Pr(r prescribed disjoint compatible edges) = (3/2n)^r(1+o(1)) | VALID | A colour-a vertex has ≈ 2n/3 admissible partners. |
| 34. (28) 3^{−ℓ}(2^ℓ+2(−1)^ℓ)(3/2)^ℓ = 1 + δ_ℓ | VALID | P(C_ℓ,3) = 2^ℓ + 2(−1)^ℓ; the planted colours on a fixed vertex set are asymptotically i.i.d. uniform. |
| 35. (29) joint factorial moments | GAP (routine) | The disjoint-cycle/overlapping-union enumeration is only sketched, as in the unbiased case. Standard. |
| 36. (30) Σ_{ℓ≥3} μ_ℓ δ_ℓ² = −2 log det(I − B/4) | VALID | tr B = tr B² = 0 (a length-2 closed non-backtracking walk would need (u,v)→(v,u)); spectral radius of B is 3 < 4. |
| 37. (31) Ihara–Bass det(I−uB) = (1−u²)⁵ det(I−uA+3u²I) | VALID | Exactly the Ihara–Bass formula with |E|−|V| = 5 and D−I = 3I. Verified numerically at u = 0.1, 0.25, 0.3 (agreement to 1e−10). |
| 38. (32) R = exp(Σ μ_ℓ δ_ℓ²) | VALID | I − A/4 + (3/16)I = (15/16)M exactly (max entrywise difference 0). Numerically Σ_{ℓ=3}^{60} μ_ℓ δ_ℓ² = 1.090094126 vs log R = 1.090094129 (difference 3e−9, pure truncation). This exact match is a strong global consistency check on Sections 3–6. |
| 39. §7 W_L martingale, E W_L² = exp(Σ_{3}^{L} μ_ℓ δ_ℓ²) | VALID | E[(1+δ)^P] = e^{μδ} for P ~ Poisson(μ). |
| 40. §7 W > 0 a.s. | VALID | δ_ℓ ∈ [−1/4, 1/4] for ℓ ≥ 3, so log(1+δ_ℓ) is finite; variances summable; second series absolutely convergent. |
| 41. §7 conditioning ⇒ Y_n → W ⇒ Pr(Z_n = 0) → 0 | GAP | This is Janson's small-subgraph-conditioning theorem. The writeup "includes the conditioning argument" but the step "at each fixed count vector the limiting conditional mean is the corresponding likelihood ratio W_L" is asserted; joint convergence of (Y_n, X_{3,n},…,X_{L,n}) is what actually needs proof, and the interchange of the L → ∞ and n → ∞ limits is glossed. All four hypotheses of Janson (1995) are, however, verified in the writeup, so this is repairable by a precise citation. |
| 42. §8 s_i + s_j = n for every base edge, hence n even and s_i = n/2 | VALID | A matching sends colour-1 vertices of fibre i bijectively onto colour-2 vertices of fibre j; K_5 contains triangles. |
| 43. §8 E[#2-colourings] = C(n,n/2)^5 · C(n,n/2)^{−10} = o(1) | VALID | Probability that one matching respects a balanced 2-colouring is ((n/2)!)²/n! = 1/C(n,n/2). Simulation: 0 bipartite lifts in 1400+ samples. |
| 44. "Scope": extension to any fixed simple 4-regular base (upper bound only) | VALID | The generalisation is consistent: for a d=4 base with |E| edges, R = (16/15)^{2|E|} det(M)^{−2} = det(I−B/4)^{−2}, which is exp(Σ μ_ℓ δ_ℓ²) by Ihara–Bass with (1−1/16)^{|E|−|V|}. Note the claim is 3-*colourability*, not χ = 3 (a bipartite base gives χ = 2), and the writeup says so. |

## Reference check

The writeup is nearly self-contained: it names no paper. The external results it uses are:

1. **Bregman–Minc, per(A) ≤ Π_v (r_v!)^{1/r_v} for 0-1 matrices, (7).** Confirmed: conjectured
   by Minc (1963), proved by Bregman (1973); entropy proof by J. Radhakrishnan,
   "An entropy proof of Bregman's theorem", JCTA 77 (1997) 161–164. The writeup's
   sketch (expose rows in random order; the rank of a row among the r_v rows meeting
   its support is uniform, giving expected log(r_v!)/r_v) is Radhakrishnan's proof.
   Statement and hypotheses used correctly.
2. **Ihara–Bass determinant identity, (31).** Proved inline; verified numerically.
3. **Local CLT / Laplace summation over lattices, Stirling, Janson's small subgraph
   conditioning.** Not cited; sketched inline (see GAPs above).

**Literature status — the decisive check.** The relevant modern reference is
J. D. Nir, X. Pérez-Giménez, *The chromatic number of random lifts of complete graphs*,
arXiv:2109.13347 (I retrieved and read the full PDF text). Their thresholds:

* Theorem 1.1: d ≥ u_k := 2 log k/(log k − log(k−1)) ⇒ a.a.s. **not** k-colourable.
  u_3 = 5.41902.
* Theorem 1.2: d < ℓ_k := 2(k−1)³ log(k−1)/(k(k−2)) ⇒ a.a.s. k-colourable.
  ℓ_3 = **3.69678**.
* Corollary 1.3(iii): d ∈ [ℓ_k, u_k) ⇒ only χ ∈ {k, k+1}.

Since d = 4 lies in [3.69678, 5.41902), **NPG explicitly leave the K_5 case open** — their
introduction says so ("it is not known for G = K_k with k ≥ 5"). So the writeup's
theorem is *not* already known from NPG.

Why NPG stop at d < ℓ_3 is exactly the point where the writeup improves on them. In
their §5.2 they bound the second-moment exponent f(A,B) (their (38)) by **relaxing the
marginal constraints (35) on B to (39)**, obtaining
g(A) = Σ_v [h(A_v) + (d/2) log(1 − 2/k + ρ(A_v))] — the *pairing-model* exponent — and
then apply Achlioptas–Naor (their Theorem 3.1), which needs d/2 < c_k, i.e. d < ℓ_k.
I verified numerically that this relaxation genuinely fails at d = 4: along
a_ii = (1+2t)/9, a_ij = (1−t)/9, g increases from 0.575364 (t=0) to 0.580944 (t=0.4),
so Â is not the maximiser of the relaxed bound. The writeup instead keeps the
matching constraint and bounds the permanent by Bregman, which is a *strictly sharper*
relaxation that is tight at U — and for d = 4 its maximiser is U. Both facts are
confirmed below. So there is no contradiction with NPG, and no priority problem.

No later paper resolving d = 4 was found (searches for 2022–2025 work on random lifts /
chromatic number / K_5 return only NPG 2021 and Farzad–Theis arXiv:1003.1527). The
earlier references [ALM02] and [FT12] exist as described in the OPG entry and are not
used in the proof.

## Computational check

Scripts in `verification_astra/scripts/chromatic_number_of_random_lifts_of_complete_graphs/`
(`python3`, numpy/scipy):

* `01_entropy.py` — Lemma 1.
  - g''(x) numeric vs formula agree to 1e−6; 3g''(1/3) = −1.125 = −9/8.
  - max of N(x) = x⁴−10x³−32x²+34x−9 on [1/3, 1) is **−1.0488 < 0**; max φ'' = −0.3099;
    max_{x ≥ 1/3} φ(x) = φ(1/3) = 1.6739764336.
  - max of g_d(x₁)+g_d(x₂)+g_d(x₃) on the simplex: for **d = 4** it is
    **1.6739764336, attained only at (1/3,1/3,1/3)** — Lemma 1 holds. For d = 3 it also
    holds; for d = 4.5, 5, 6 the uniform point is *not* the maximum (e.g. d = 5:
    1.86257 at (0.0916, 0.0916, 0.8167) vs 1.81782 at uniform). The local criterion
    g_d''(1/3) < 0 is d < 96/21 = 4.5714, so d = 4 is inside and d = 5 outside — i.e.
    the method is specific to the 4-regular case, as the writeup's "this is exactly
    where 4-regularity is used" says.
  - Direct 9-variable maximisation of F over row-stochastic/3 matrices returns
    max F = 0.5753641449 = F(U) = 2log(4/3).
* `02b_exact_exponent_fast.py`, `05_bregman_check.py` — the *exact* second-moment
  exponent, bypassing the writeup's bound entirely. From per(A)/n! by Stirling,
  λ(ρ,σ) := lim (1/n) log q_n(ρ,σ) = −h(ρ) − h(σ) + H(B*), B* the maximum-entropy
  coupling of (ρ,σ) supported on {(i,j,i',j') : i≠i', j≠j'} (computed by Sinkhorn).
  This is exactly NPG's f(A,B) maximised over B.
  - λ(U,U) = −0.810930216 = log(4/9); Φ(U,…,U) = 2.87682072 = 2(5log3 + 10log(2/3)),
    i.e. the exponent of (E Z_n)². Encoding validated.
  - **(8) holds**: max over 19851 random doubly-stochastic pairs of
    λ(a,b) − Σ a log(1/3+b) = **−1.38e−5** (≤ 0).
  - **(10) holds**: max of λ(a,b) − (L(a)+L(b))/2 = **−1.35e−3** (≤ 0).
  - **The exact per-fibre exponent h(ρ) + 2λ(ρ,ρ) is maximised at U**: global search
    returns 0.57536414 = 2log(4/3) at U; 20000 random restarts never exceed it
    (best 0.57525791 at a matrix within 0.006 of U). Along the family above it is
    strictly decreasing (0.575364 → 0.568501 at t = 0.2 → 0.287682 at t = 1),
    whereas NPG's relaxed g increases. So the conclusion of Lemma 1 is true for the
    *exact* exponent too, not only for the writeup's upper bound.
* `03_cycles_variance.py` — Sections 3–6.
  - spec(P₀) = (−1/2, −1/2, 1); det_{1⊥}(I−P₀²)^{−1/2} = 1.3333 = 4/3.
  - (9/16)·det_{1⊥}(I−P₁²)^{−1/2} = 1.13777778 = (16/15)².
  - eig(M) = (0.2, 1.5333×4); det M = 1.10554469; **R = 2.9745540512**,
    log R = 1.0900941290.
  - B is 20×20 with row sums 3; tr(B^ℓ) = 0, 0, 60, 120, 120, 780, 2520, 6120 for
    ℓ = 1..8; μ₃ = 10, μ₄ = 15, μ₅ = 12, μ₆ = 65.
  - **Σ_{ℓ=3}^{60} μ_ℓ δ_ℓ² = 1.090094126 vs log R = 1.090094129** — the writeup's
    exact variance match (32) is confirmed (residual 3e−9 is truncation).
    −2 log det(I − B/4) = 1.0900941290 to 10 digits.
  - Ihara–Bass verified at u = 0.1, 0.25, 0.3; I − A/4 + (3/16)I − (15/16)M = 0 exactly.
  - Exact E Z_n for n ≤ 30 (permanents by inclusion–exclusion):
    a_n/[(4/3)(2/3)^n] = 0.8438, 0.9492, 0.9611, 0.9717, 0.9773, 0.9812, 0.9859,
    0.9888 → 1, and E Z_n / [n^{−5}(4/3)^{5n}] = 0.43, 2.35, 3.19, 3.91, 4.37, 4.72,
    5.19, 5.49, converging to the predicted 6.87.
* `04_simulate_lifts.py` — random n-lifts of K_5, exact 3-colourability by
  degree-<3 kernelisation + MRV/forward-checking backtracking:

  | n | vertices | trials | 3-colourable | fraction | mean triangles | mean C₄ | mean C₅ | bipartite |
  |---|---|---|---|---|---|---|---|---|
  | 3 | 15 | 400 | 211 | 0.527 | 9.85 | 15.14 | 11.84 | 0 |
  | 5 | 25 | 400 | 342 | 0.855 | 9.86 | 14.75 | 11.72 | 0 |
  | 8 | 40 | 300 | 275 | 0.917 | 10.20 | 15.14 | 12.13 | 0 |
  | 12 | 60 | 300 | 293 | 0.977 | 9.97 | 15.15 | 12.07 | 0 |
  | 20 | 100 | 200 | 200 | 1.000 | 9.79 | 14.94 | 12.09 | 0 |

  The fraction rises monotonically to 1, consistent with a.a.s. 3-colourability;
  the cycle means match μ₃ = 10, μ₄ = 15, μ₅ = 12; no bipartite lift ever occurred.

Nothing failed. Every explicit constant in the writeup (4/3, (16/15)², 1/5 and 23/15,
R = 25(16/15)^20(15/23)^8, μ₃ = 10, μ₄ = 15, the (32) identity) reproduces exactly.

## Caveats

1. **Two sketched analytic steps.** Lemma 2's uniform local CLT (step 20) and the
   small-subgraph-conditioning limit (step 41) are the only places where the writeup
   asserts rather than proves. Both are standard: NPG spend most of their ~35 pages on
   the analogues (they cite Greenhill–Janson–Ruciński for the Laplace-summation/local
   limit step and Robinson–Wormald/Janson for the conditioning). A referee would
   require these to be written out or replaced by precise citations with hypotheses
   checked. I judge them repairable, not holes, because the writeup does verify all
   four Janson hypotheses explicitly and because Lemma 2's formula passes the
   (α,β)-symmetry test and reproduces (32) exactly.
2. **The joint factorial-moment computation (29)** is a one-sentence "the same
   disjoint-cycle and overlapping-union enumeration"; routine but unwritten.
3. **(6)**, the passage from exact row sums 1/3 to the rounded p, uses an unproved
   continuity-of-entropy estimate; harmless (the resulting O(log n) is dominated by
   exp(−c n^{1/5})), but it is where the "all integers n, not merely multiples of 3"
   claim ultimately rests. NPG needed a separate section (their §7) for the
   non-divisible case; the writeup's set-up is general from the start, so this is
   plausible, but it is the thinnest part of the "for all n" claim.
4. **Non-primitive closed walks.** μ_ℓ = tr(B^ℓ)/(2ℓ) counts closed non-backtracking
   walks including proper powers (e.g. a triangle traversed twice for ℓ = 6), whose
   symmetry group is smaller than 2ℓ. The writeup's "dividing rooted oriented cycles
   by 2ℓ" does not address this. I checked ℓ = 6 by hand: doubled triangles contribute
   60 to tr(B⁶) = 780, i.e. 5 = 10 × E[#2-cycles of a uniform permutation] to μ₆ = 65,
   which is exactly right — so the formula survives, but the justification as written
   is incomplete. Also, degenerate lifts (fixed points giving a non-simple walk) are
   swept into the "(1+O(1/n))".
5. **Scope of the claim.** The theorem is for K_5 only; the OPG entry's more general
   question about K_n is untouched. The "Scope" section's extension to arbitrary fixed
   simple 4-regular bases gives 3-*colourability* (χ ≤ 3) only, which the writeup
   states correctly — for a bipartite base χ = 2, so "χ = 3" would be false there.
6. **The method is knife-edge in d.** Lemma 1 holds for d ≤ 4 and fails for d ≥ 5
   (the local criterion is d < 96/21 = 4.571). So the companion open case d = 5
   (lifts of K_6, also in NPG's gap [ℓ₃, u₃)) is *not* resolved by this argument. The
   writeup does not claim it, but a reader might over-read the "Scope" paragraph.
7. **Edge cases.** n odd is handled (Section 8 forces n even for a 2-colouring, and
   the balanced-colouring set-up allows t_a = ⌈n/3⌉ or ⌊n/3⌋). Small n is irrelevant
   to an a.a.s. claim; my simulation shows 47% of 3-lifts are not 3-colourable, which
   is consistent. Disconnected lifts occur with probability o(1) and change nothing.
8. **Novelty self-caveat.** The writeup's own caveat ("Novelty relative to the full
   cited literature has not been independently checked") is now discharged: I checked
   it, and the result is new relative to NPG 2021 and everything I could find.

## Referee summary

I set out to break this writeup and could not. The suspicious step — a second-moment
argument succeeding exactly where Nir–Pérez-Giménez (arXiv:2109.13347) stop — turns out
to be a legitimate and identifiable improvement rather than an error: NPG bound the
lift's second-moment exponent by *dropping* the perfect-matching marginal constraints
(their (35) → (39)), which turns the problem into the pairing-model/Achlioptas–Naor
optimisation and forces d < ℓ₃ = 3.697; the writeup instead keeps the matching and
bounds the permanent by Bregman's inequality, a relaxation that is tight at the uniform
overlap and whose maximiser at d = 4 is the uniform overlap. I re-derived every formula
in the writeup independently — (1), (2), (3), the reduction to g, the φ'' numerator
(by hand expansion), (8), (10), (12), the Σ₀ covariance, (17), (18), (20) (including
the lattice covolume 729 and an independent hypergeometric-variance cross-check),
(21) (including the (16/15)² prefactor and an (α,β)-symmetry consistency test), (22)–(25),
(30), (31), (32), and Section 8 — and found no arithmetic or algebraic error. I also
computed the *exact* second-moment exponent (max-entropy couplings, bypassing the
writeup's bound) and confirmed both that (8) and (10) hold over ~20000 random overlap
pairs and that the exact exponent is globally maximised at the uniform overlap; the
variance identity Σ μ_ℓ δ_ℓ² = log R = 1.0900941 matches to 3e−9; and simulated random
lifts are 3-colourable in 100% of 200 trials at n = 20 with cycle counts matching
μ₃ = 10, μ₄ = 15, μ₅ = 12. What keeps this from CONFIRMED is not a suspected error but
missing rigour in two standard technical steps the writeup chose to sketch rather than
cite — the uniform local limit theorem of Lemma 2 and the passage from the four verified
Janson hypotheses to Z_n > 0 a.a.s. in Section 7 — plus the incompletely justified
treatment of non-primitive closed walks in μ_ℓ. Those are, in my judgement, routine and
repairable, so: **MINOR_GAPS**, with the recommendation that the writeup be resubmitted
with §3 and §7 either written out or reduced to precise citations
(Greenhill–Janson–Ruciński; Janson 1995 / Wormald's survey). If it survives that, it is
a genuine resolution of the Amit–Linial–Matoušek K_5 question and is publishable.
