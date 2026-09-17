import sys, itertools
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/1904.02595__00')
from core import build, IR, alpha

def name(factors):
    return " x ".join("K(" + ",".join(map(str, f)) + ")" for f in factors)

cases = []
# single factors
for f in [[1,1,1],[1,1,1,1],[2,1,1],[2,2,1],[2,2,2],[3,2,1],[3,3,3],[1,1,1,1,1]]:
    cases.append([f])
# two factors
twos = [[1,1],[1,1,1],[2,1],[2,2],[2,1,1],[1,1,1,1],[2,2,1],[3,1,1]]
for a in twos:
    for b in twos:
        if sum(a)*sum(b) <= 18:
            cases.append([a,b])
# three factors
for a in [[1,1],[1,1,1],[2,1]]:
    for b in [[1,1],[1,1,1],[2,1]]:
        for c in [[1,1],[1,1,1],[2,1]]:
            if sum(a)*sum(b)*sum(c) <= 18:
                cases.append([a,b,c])

seen = set()
bad = []
for factors in cases:
    key = tuple(tuple(sorted(f, reverse=True)) for f in factors)
    if key in seen: continue
    seen.add(key)
    verts, N, Nc = build(factors)
    n = len(verts)
    ir, S = IR(Nc, n)
    al, _ = alpha(factors)
    flag = "OK " if ir == al else "MISMATCH"
    if ir != al: bad.append((factors, ir, al))
    print(f"{flag} {name(factors):40s} |V|={n:3d} alpha={al:3d} IR={ir:3d}")
print()
print("mismatches:", bad)
