"""Monte Carlo verification of the claims in attacks/2106.14762__00/output.md.

Simulates runsort on uniform random permutations and checks:
  A. Run-starter intensity at value z is ~ (1-z) dz            [step 2, eq (7)]
  B. Mean run length given starter value z is ~ e^{1-z}        [eq (12)]
  C. Off-diagonal density of eta at (z,y), z<y, is (1-z)e^{y-z} [eq (8)]
  D. H_n(z) (size-biased starter CDF) ~ H(z)=z e^{1-z}, sup err [eqs (17),(18)]
  E. |p_n(i)/n - H_n(A_n(i)/n)| <= L_n/n, and L_n is small     [eqs (4),(5)]
  F. Horizontal uniformity of runsort permuton: within a y-strip,
     interior x's are uniform on (0, y e^{1-y}); interior mass ~ y,
     boundary mass ~ 1-y; 2D density ~ e^{y-1}                 [eqs (1),(20)]
"""
import numpy as np

rng = np.random.default_rng(20260902)

N = 1_000_000
TRIALS = 8

def one_trial(n):
    pi = rng.permutation(n) + 1  # values 1..n
    # run starts: position 0, or previous value larger
    starts = np.empty(n, dtype=bool)
    starts[0] = True
    starts[1:] = pi[:-1] > pi[1:]
    run_id = np.cumsum(starts) - 1
    starter_vals = pi[starts]           # first value of each run, in position order
    A = starter_vals[run_id]            # A[i] = first value of run containing position i
    # runsort = stable sort of entries by (starter value, original position)
    order = np.lexsort((np.arange(n), A))
    sigma = pi[order]                   # runsorted permutation
    # position after runsort for each original index
    p = np.empty(n, dtype=np.int64)
    p[order] = np.arange(1, n + 1)
    # run lengths
    run_lengths = np.diff(np.flatnonzero(np.append(starts, True)))
    Ln = run_lengths.max()
    return pi, A, p, sigma, starter_vals, run_lengths, run_id, Ln

# accumulators
nbins = 20
starter_count = np.zeros(nbins)              # A: run-starter count per value bin
runlen_sum = np.zeros(nbins); runlen_cnt = np.zeros(nbins)  # B
eta_hist = np.zeros((nbins, nbins))          # C: off-diagonal (non-starter) entries (A/n, v/n)
Hgrid = np.linspace(0, 1, 101)
H_sup_errs = []                              # D
bound_ok = True; Lns = []                    # E
# F: y-strips
strips = [(0.15, 0.20), (0.40, 0.45), (0.60, 0.65), (0.85, 0.90)]
strip_interior_x = {s: [] for s in strips}   # x's strictly below curve (with margin)
strip_interior_mass = {s: 0.0 for s in strips}
strip_total = {s: 0.0 for s in strips}
# 2D permuton histogram
perm_hist = np.zeros((nbins, nbins))

for t in range(TRIALS):
    pi, A, p, sigma, starter_vals, run_lengths, run_id, Ln = one_trial(N)
    n = N
    Lns.append(Ln)
    z = starter_vals / n
    # A: starter intensity
    starter_count += np.histogram(z, bins=nbins, range=(0, 1))[0]
    # B: run length vs starter value
    idx = np.minimum((z * nbins).astype(int), nbins - 1)
    np.add.at(runlen_sum, idx, run_lengths)
    np.add.at(runlen_cnt, idx, 1)
    # C: eta off-diagonal = non-starter entries
    starts_mask = np.zeros(n, dtype=bool)
    starts_mask[0] = True; starts_mask[1:] = pi[:-1] > pi[1:]
    ns = ~starts_mask
    eta_hist += np.histogram2d(A[ns] / n, pi[ns] / n, bins=nbins, range=[[0, 1], [0, 1]])[0]
    # D: H_n vs H  (size-biased CDF of starters)
    Avals_sorted = np.sort(A) / n
    Hn = np.searchsorted(Avals_sorted, Hgrid, side='right') / n
    H = Hgrid * np.exp(1 - Hgrid)
    H_sup_errs.append(np.max(np.abs(Hn - H)))
    # E: bound (4)
    Asort = np.sort(A)
    Hn_at_A = np.searchsorted(Asort, A, side='right') / n
    dev = np.max(np.abs(p / n - Hn_at_A))
    if dev > Ln / n + 1e-12:
        bound_ok = False
        print(f"  BOUND (4) VIOLATED: dev={dev}, Ln/n={Ln/n}")
    # F: permuton strips (use runsorted plot: point (j/n, sigma(j)/n))
    xs = np.arange(1, n + 1) / n
    ys = sigma / n
    perm_hist += np.histogram2d(xs, ys, bins=nbins, range=[[0, 1], [0, 1]])[0]
    for (c, d) in strips:
        sel = (ys >= c) & (ys < d)
        strip_total[(c, d)] += sel.sum()
        xc = c * np.exp(1 - c)  # curve at bottom of strip (min over strip since y<1 => increasing? not always)
        # curve x_c(y)=y e^{1-y} is increasing on [0,1]; interior means x < y e^{1-y}
        cut = ys[sel] * np.exp(1 - ys[sel])
        xin = xs[sel][xs[sel] < cut - 0.01]   # margin 0.01 away from boundary
        strip_interior_mass[(c, d)] += (xs[sel] < cut).sum()
        strip_interior_x[(c, d)].append(xin)

tot = TRIALS * N
print(f"n = {N}, trials = {TRIALS}")
print(f"\nE. max run lengths per trial: {Lns} (all << n; bound (4) held: {bound_ok})")
print(f"D. sup_z |H_n(z) - z e^(1-z)| per trial: {[f'{e:.5f}' for e in H_sup_errs]}")

print("\nA. run-starter intensity per value bin (empirical vs (1-z)dz):")
centers = (np.arange(nbins) + 0.5) / nbins
emp = starter_count / tot * nbins
th = 1 - centers
th[0] = 1 - centers[0]  # boundary effect at z~0: position 1 is always a starter (adds O(1/n), negligible)
maxrel = np.max(np.abs(emp - th) / th)
print(f"   max relative error over bins: {maxrel:.4f}")
for i in range(0, nbins, 5):
    print(f"   z~{centers[i]:.3f}: emp {emp[i]:.5f}  theory {th[i]:.5f}")

print("\nB. mean run length given starter value (empirical vs e^(1-z)):")
mrl = runlen_sum / np.maximum(runlen_cnt, 1)
thl = np.exp(1 - centers)
maxrel = np.max(np.abs(mrl - thl) / thl)
print(f"   max relative error over bins: {maxrel:.4f}")
for i in range(0, nbins, 5):
    print(f"   z~{centers[i]:.3f}: emp {mrl[i]:.5f}  theory {thl[i]:.5f}")

print("\nC. eta off-diagonal density (empirical vs (1-z)e^(y-z)), off-diagonal bins only:")
errs = []
for i in range(nbins):
    for j in range(nbins):
        if j > i:  # z-bin strictly below y-bin => fully off-diagonal
            zc, yc = centers[i], centers[j]
            emp_d = eta_hist[i, j] / tot * nbins * nbins
            th_d = (1 - zc) * np.exp(yc - zc)
            if th_d > 1e-3:
                errs.append(abs(emp_d - th_d) / th_d)
print(f"   {len(errs)} off-diagonal bins, max relative error: {max(errs):.4f}, mean: {np.mean(errs):.4f}")

print("\nF. horizontal uniformity in y-strips of runsort permuton:")
for (c, d) in strips:
    ymid = (c + d) / 2
    xc_mid = ymid * np.exp(1 - ymid)
    tot_s = strip_total[(c, d)]
    im = strip_interior_mass[(c, d)] / tot_s
    # theory: interior mass fraction = average of y over strip / 1 = ymid (since marginal uniform)
    xin = np.concatenate(strip_interior_x[(c, d)])
    # interior x should be uniform on (0, cut); rescale by the strip's own cut per point already applied;
    # test uniformity of xin on (0, xc_mid - 0.01) via 10-bin chi-square-style max deviation
    hb, edges = np.histogram(xin, bins=10, range=(0, xc_mid - 0.01))
    dens = hb / len(xin) * 10
    print(f"   y in ({c},{d}): interior mass frac emp {im:.4f} vs theory ~{ymid:.4f}; "
          f"boundary frac emp {1-im:.4f} vs {1-ymid:.4f}")
    print(f"      interior x-density over 10 equal bins (should all be ~1.000): "
          f"{np.array2string(dens, precision=3)}")
    # 2D density check at strip: e^{y-1}
    print(f"      implied interior density emp {im/xc_mid:.4f} vs e^(y-1) = {np.exp(ymid-1):.4f}")

print("\nDONE")
