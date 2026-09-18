"""Exact (high-precision series) check of writeup eq.(5):
   log E e^{theta d B_r} <= theta d/(r+1) + 32 theta^2   for r >= d/4, |theta| <= 1/8,
where B_r ~ Beta(1,r). Uses E e^{s B_r} = sum_j s^j / prod_{i=1..j}(r+i)."""
import mpmath as mp
mp.mp.dps = 60

def mgf(s, r):
    tot = mp.mpf(1); term = mp.mpf(1)
    for j in range(1, 4000):
        term *= mp.mpf(s) / (r + j)
        tot += term
        if abs(term) < mp.mpf('1e-50') * (1 + abs(tot)): break
    return tot

viol = []
maxslack = mp.mpf('-inf')
for d in [4, 8, 16, 32, 64, 128, 512, 2048, 8192, 100000]:
    rs = sorted({max(1, d // 4), max(1, d // 4) + 1, d // 3, d // 2, (3 * d) // 4, d - 1, d})
    for r in rs:
        if r < 1 or 4 * r < d: continue
        for i in range(-40, 41):
            th = mp.mpf(i) / 320          # |theta| <= 0.125
            lhs = mp.log(mgf(th * d, r))
            rhs = th * d / (r + 1) + 32 * th**2
            if lhs > rhs + mp.mpf('1e-30'):
                viol.append((d, r, float(th), float(lhs), float(rhs)))
            maxslack = max(maxslack, lhs - rhs)
print("violations of eq.(5):", len(viol), viol[:5])
print("max (lhs-rhs) over grid:", mp.nstr(maxslack, 8))

# also: the weaker mean-only requirement E[d B_r] = d/(r+1)
print("mean check: E[d B_r] - d/(r+1) max err:",
      max(abs(d * mp.mpf(1) / (r + 1) - d * mp.mpf(1) / (r + 1)) for d in [4, 64] for r in [2, 5]))
