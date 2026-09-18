"""(i) Cross-check the vectorised build_F/cycles_of in planted_sim.py against the
       independent brute-force implementation in identity_and_moments.py.
   (ii) Independently test writeup eq.(5):  W(x) <= e^{9/4} = 9.48774  on the cube,
        by direct maximisation of log W = S^2/2 + sum_{v<w not in M} log(1-x_v x_w),
        over random x and over the worst-case-looking all-equal x_v = c.
"""
import math, random
import numpy as np
from planted_sim import build_F, cycles_of
from identity_and_moments import Ff, cycles as bcycles

rng = random.Random(4)
mism = 0; tested = 0; cmism = 0
for _ in range(4000):
    n = random.choice([6, 8, 10])
    U = [[rng.random() for _ in range(n)] for _ in range(n)]
    part = [v ^ 1 for v in range(n)]           # M = (0,1),(2,3),...
    x = [U[v][part[v]] for v in range(n)]
    # brute force
    _, fb, Fb = Ff(part, U, n)
    cb = sorted(tuple(sorted(c)) for c in bcycles(Fb, n))
    # vectorised
    Un = np.array(U); xn = np.array(x)
    fv, Fv, has = build_F(n, xn, Un)
    cv = sorted(tuple(sorted(c)) for c in cycles_of(Fv, has, n))
    tested += 1
    for v in range(n):
        if (fb[v] is None) != (not has[v]) or (fb[v] is not None and fb[v] != fv[v]):
            mism += 1
    if cb != cv: cmism += 1
print(f"(i) build_F cross-check over {tested} random instances (n in 6,8,10):")
print(f"    f-mismatches: {mism}   cycle-set mismatches: {cmism}")

print("(ii) W <= e^{9/4} = %.5f ?" % math.exp(9/4))
best = 0.0; arg = None
for n in [4, 6, 8, 10, 20, 50, 100, 200]:
    iu = np.triu_indices(n, 1)
    inM = (iu[1] == iu[0] + 1) & (iu[0] % 2 == 0); notM = ~inM
    loc = 0.0
    r = np.random.default_rng(7)
    for _ in range(4000):
        # mixture of proposal shapes, incl. the LLN-typical scale sqrt(2/n)
        mode = r.integers(0, 4)
        if mode == 0: x = r.random(n)
        elif mode == 1: x = r.random(n) * math.sqrt(2.0/n) * r.uniform(0.2, 4)
        elif mode == 2: x = np.full(n, min(0.999, r.uniform(0, 3)/math.sqrt(n)))
        else: x = r.exponential(size=n) * r.uniform(0.2, 4) / math.sqrt(n)
        x = np.clip(x, 0, 1 - 1e-12)
        S = x.sum()
        P = np.outer(x, x)[iu][notM]
        logW = 0.5*S*S + np.log1p(-P).sum()
        if logW > loc: loc = logW
        if logW > best: best = logW; arg = (n, float(x.mean()), float(S))
    print(f"    n={n:4d}  max log W found = {loc:8.5f}   (W = {math.exp(loc):8.5f})")
print(f"    global max log W = {best:.5f} (W={math.exp(best):.5f})  bound 9/4 = 2.25 "
      f"(W bound {math.exp(2.25):.5f})  -> {'HOLDS' if best <= 2.25 + 1e-9 else 'VIOLATED'}")
print(f"    argmax approx: n,mean(x),S = {arg}")
