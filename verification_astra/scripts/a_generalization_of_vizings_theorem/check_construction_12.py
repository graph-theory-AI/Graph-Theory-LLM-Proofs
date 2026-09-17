"""
Brute-force check of section 1.2 of the writeup:
 - weighted regularity of K (old and new vertices both have weighted degree D/x),
 - "every perfect matching of K uses exactly u auxiliary edges",
 - identity (7):  Z = a_m(F) * b!/((s-1)!)^u * w^u.
Small explicit F's (linear, D-regular) where everything can be enumerated.
"""
import itertools, math
from math import comb, factorial

def perfect_matchings_count_and_Z(L, edges, w):
    """edges: list of frozensets. Returns (#PM, Z, #PM using k auxiliary edges dict)."""
    full = frozenset(range(L))
    byv = {v: [e for e in edges if v in e] for v in range(L)}
    res = {"n": 0, "Z": 0.0, "aux": {}}
    def rec(remaining, prod, naux):
        if not remaining:
            res["n"] += 1; res["Z"] += prod
            res["aux"][naux] = res["aux"].get(naux, 0) + 1
            return
        v = min(remaining)
        for e in byv[v]:
            if e <= remaining:
                rec(remaining - e, prod * w[e], naux + (1 if w[e] != 1.0 else 0))
    rec(full, 1.0, 0)
    return res

def matchings_of_size(edges, m):
    """count matchings of exactly m pairwise disjoint edges"""
    cnt = 0
    for comb_ in itertools.combinations(edges, m):
        s = set()
        ok = True
        for e in comb_:
            if s & e: ok = False; break
            s |= e
        if ok: cnt += 1
    return cnt

def run(name, s, N, Fedges, D, m):
    x = s * m / N
    u = N - s*m
    b = (s-1)*u
    assert b >= s-1
    w_aux = ((1-x)*D/x) / comb(b, s-1)
    # vertices 0..N-1 old, N..N+b-1 new
    B = list(range(N, N+b))
    edges = [frozenset(e) for e in Fedges]
    w = {e: 1.0 for e in edges}
    for a in range(N):
        for C in itertools.combinations(B, s-1):
            e = frozenset((a,)+C)
            edges.append(e); w[e] = w_aux
    L = N + b
    # weighted degrees
    degs = {v: sum(w[e] for e in edges if v in e) for v in range(L)}
    dold = set(round(degs[v], 9) for v in range(N))
    dnew = set(round(degs[v], 9) for v in range(N, L))
    res = perfect_matchings_count_and_Z(L, edges, w)
    am = matchings_of_size(Fedges, m)
    predicted = am * factorial(b) / (factorial(s-1)**u) * (w_aux**u)
    predicted_count = am * factorial(b) / (factorial(s-1)**u)
    aux_used = sorted(res["aux"].keys())
    print(f"--- {name}: s={s} N={N} D={D} m={m} x={x:.4f} u={u} b={b} w={w_aux:.6g}")
    print(f"    weighted deg (old) = {dold}, (new) = {dnew}, claimed D/x = {D/x:.6f}")
    print(f"    #PM(K) = {res['n']}   predicted a_m*b!/((s-1)!)^u = {predicted_count:.0f}"
          f"   {'MATCH' if abs(res['n']-predicted_count)<0.5 else 'MISMATCH'}")
    print(f"    a_m(F) = {am};  #aux edges used per PM: {aux_used} (claim: all = u = {u})"
          f"   {'OK' if aux_used==[u] else 'FAIL'}")
    print(f"    Z = {res['Z']:.10g}   predicted (7) = {predicted:.10g}"
          f"   {'MATCH' if abs(res['Z']-predicted)<=1e-6*max(1,abs(predicted)) else 'MISMATCH'}")

if __name__ == "__main__":
    # C_4 : s=2, N=4, D=2, linear
    C4 = [frozenset((i,(i+1)%4)) for i in range(4)]
    run("C_4", 2, 4, C4, 2, 1)
    # C_6
    C6 = [frozenset((i,(i+1)%6)) for i in range(6)]
    run("C_6", 2, 6, C6, 2, 1)
    # K_4 : D=3
    K4 = [frozenset(p) for p in itertools.combinations(range(4),2)]
    run("K_4", 2, 4, K4, 3, 1)
    # Petersen-like: K_{3,3}, D=3, N=6
    K33 = [frozenset((i,3+j)) for i in range(3) for j in range(3)]
    run("K_3,3", 2, 6, K33, 3, 1)
    # AG(2,3) Steiner triple system: s=3, N=9, D=4, linear
    pts=[(i,j) for i in range(3) for j in range(3)]; idx={p:i for i,p in enumerate(pts)}
    lines=set()
    for a in pts:
        for bb in pts:
            if a==bb: continue
            c=((2*bb[0]-a[0])%3,(2*bb[1]-a[1])%3)
            lines.add(frozenset((idx[a],idx[bb],idx[c])))
    lines=[l for l in lines if len(l)==3]
    run("AG(2,3)", 3, 9, lines, 4, 2)
