"""END-TO-END test of Lemma 6 (the step the writeup's soundness rests on).

For a NO-instance of two-linkage and random acyclic subgraphs H of F_h we execute the
writeup's whole compression pipeline and check every claimed property:

  (1) replace each core's H-restriction by the Lemma-3 oriented sub-forest of Q or Q/xy
      with the SAME port relation      -> must stay acyclic, must not lose requests
  (2) contract the remaining central bridges x_w y_w
                                       -> must stay acyclic, must not lose requests
  (3) suppress the degree-2 subdivision vertices; check that the resulting arcs are all
      edges of B_h and that the digraph is acyclic; take a topological order of B_h
                                       -> must not lose requests
  (4) final count must be <= OPT(B_h)  (exhaustive for h<=3, DP upper bound above)
"""
import itertools, random, sys
from collections import defaultdict
from construction import (G_NO, core_arcs, DSU, hypercube_requests, realized, adj_of, reach)

PORTS = ['a', 'b', 'l', 'r']

# ---------- witnesses: port-relation -> oriented sub-forest of Q or Q/xy ----------
def _port_reach(arcs, ports):
    ad = adj_of(arcs)
    rel = set()
    for p in ports:
        for q in reach(ad, p):
            if q in ports and q != p:
                rel.add((p, q))
    return frozenset(rel)

def witness_table():
    """maps a port relation to ('Q', [oriented edges]) or ('S', [oriented edges])"""
    tab = {}
    Qe = [('a','x'),('b','x'),('x','y'),('y','l'),('y','r')]
    for st in itertools.product([0,1,2], repeat=len(Qe)):
        arcs = []
        for (u,v), s in zip(Qe, st):
            if s == 1: arcs.append((u,v))
            elif s == 2: arcs.append((v,u))
        rel = _port_reach(arcs, PORTS)
        tab.setdefault(rel, ('Q', arcs))
    Se = [('a','c'),('b','c'),('c','l'),('c','r')]
    for st in itertools.product([0,1,2], repeat=len(Se)):
        arcs = []
        for (u,v), s in zip(Se, st):
            if s == 1: arcs.append((u,v))
            elif s == 2: arcs.append((v,u))
        rel = _port_reach(arcs, PORTS)
        tab.setdefault(rel, ('S', arcs))
    return tab
WIT = witness_table()

# ---------- build F_h keeping per-core bookkeeping ----------
def build(G, h):
    dsu = DSU(); arcs = []; verts = set(); marked = {}; cores = {}; bases = {}
    A_ = lambda w: ('A', w); B_ = lambda w: ('B', w)
    def rec(w, d):
        verts.add(A_(w)); verts.add(B_(w))
        if d == 0:
            z = ('Z', w); verts.add(z); marked[w] = z
            e = [(A_(w), z), (z, A_(w)), (z, B_(w)), (B_(w), z)]
            arcs.extend(e); bases[w] = e
        else:
            rec(w+'0', d-1); rec(w+'1', d-1)
            dsu.union(B_(w+'0'), A_(w+'1'))
            ell = A_(w+'0'); r = B_(w+'1')
            ca, cv = core_arcs(G, w, A_(w), B_(w), ell, r)
            arcs.extend(ca); verts.update(cv)
            cores[w] = dict(arcs=ca, interior=cv, ports={'a':A_(w),'b':B_(w),'l':ell,'r':r})
    rec('', h)
    f = dsu.find
    V = {f(v) for v in verts}
    Arcs = {(f(u), f(v)) for u, v in arcs}
    M = {w: f(z) for w, z in marked.items()}
    for w, c in cores.items():
        c['arcs'] = [(f(u), f(v)) for u, v in c['arcs']]
        c['interior'] = [f(v) for v in c['interior']]
        c['ports'] = {k: f(v) for k, v in c['ports'].items()}
    for w in bases:
        bases[w] = [(f(u), f(v)) for u, v in bases[w]]
    return V, sorted(Arcs), M, cores, bases, f

def topo(V, arcs):
    """returns a topological order, or None if cyclic"""
    out = defaultdict(list); indeg = defaultdict(int)
    Vs = set(V)
    for u, v in arcs:
        out[u].append(v); indeg[v] += 1
    S = [v for v in Vs if indeg[v] == 0]; order = []
    while S:
        u = S.pop(); order.append(u)
        for v in out[u]:
            indeg[v] -= 1
            if indeg[v] == 0: S.append(v)
    return order if len(order) == len(Vs) else None

def count(V, arcs, M, R):
    o = topo(V, arcs)
    if o is None: return None
    return realized(o, arcs, sorted(M.values()), R)

def run(h, trials, seed):
    V, A, M, cores, bases, f = build(G_NO, h)
    R = hypercube_requests(M, h)
    rng = random.Random(seed)
    Vl = sorted(V, key=repr)
    worst = 0; fails = []
    for t in range(trials):
        # random acyclic subgraph H = forward subgraph of a random enumeration
        perm = Vl[:]; rng.shuffle(perm)
        pos = {v: i for i, v in enumerate(perm)}
        H = [(u, v) for u, v in A if pos[u] < pos[v]]
        c0 = count(V, H, M, R)
        assert c0 is not None

        # ---- (1) replace every core by its Lemma-3 forest ----
        arcs1 = []; newV = set()
        for w, base in bases.items():
            for e in base:
                if e in set(H): arcs1.append(e)
        Hs = set(H)
        contract_pairs = []
        for w, c in cores.items():
            sub = [e for e in c['arcs'] if e in Hs]
            local = c['interior'] + list(c['ports'].values())
            inv = {v: k for k, v in c['ports'].items()}
            ad = adj_of(sub); rel = set()
            for k, p in c['ports'].items():
                for q in reach(ad, p):
                    if q in inv and q != p: rel.add((k, inv[q]))
            rel = frozenset(rel)
            if rel not in WIT:
                fails.append(('LEMMA3 relation not representable', w, rel)); continue
            kind, oriented = WIT[rel]
            xw = ('x', w); yw = ('y', w); cw = ('c', w)
            nm = dict(c['ports']); nm.update({'x': xw, 'y': yw, 'c': cw})
            arcs1 += [(nm[u], nm[v]) for u, v in oriented]
            if kind == 'Q':
                newV |= {xw, yw}; contract_pairs.append((w, xw, yw, cw))
            else:
                newV.add(cw)
        V1 = (set(V) - {v for c in cores.values() for v in c['interior']}) | newV
        c1 = count(V1, arcs1, M, R)
        if c1 is None: fails.append(('step1 cyclic', t)); continue
        if c1 < c0: fails.append(('step1 lost requests', t, c0, c1))

        # ---- (2) contract central bridges ----
        rep = {}
        for w, xw, yw, cw in contract_pairs:
            rep[xw] = cw; rep[yw] = cw
        g = lambda v: rep.get(v, v)
        arcs2 = {(g(u), g(v)) for u, v in arcs1 if g(u) != g(v)}
        V2 = {g(v) for v in V1}
        c2 = count(V2, arcs2, M, R)
        if c2 is None: fails.append(('step2 cyclic', t)); continue
        if c2 < c1: fails.append(('step2 lost requests', t, c1, c2))

        # ---- (3) suppress degree-2 subdivision vertices ----
        main = {}
        for w in cores: main[('c', w)] = w
        for w, z in M.items(): main[z] = w
        subdiv = V2 - set(main) - {f(('A','')), f(('B',''))}
        out2 = defaultdict(list); inn2 = defaultdict(list)
        for u, v in arcs2:
            out2[u].append(v); inn2[v].append(u)
        # degree check
        for s in subdiv:
            deg = len({x for x in out2[s]} | {x for x in inn2[s]})
            if deg > 2: fails.append(('subdivision vertex of degree>2', s, deg))
        arcs3 = set()
        for s in subdiv:
            for u in inn2[s]:
                for v in out2[s]:
                    if u in main and v in main and u != v:
                        arcs3.add((main[u], main[v]))
        # every arc must be an edge of B_h
        Bedges = set()
        for w in cores:
            for e in [(w, w+'0'), (w, w+'1'), (w+'0', w+'1')]:
                Bedges.add(frozenset(e))
        for u, v in arcs3:
            if frozenset((u, v)) not in Bedges:
                fails.append(('arc not a B_h edge', u, v))
        Bverts = set(main.values())
        o3 = topo(Bverts, arcs3)
        if o3 is None: fails.append(('step3 cyclic', t)); continue
        Rb = [(main[x], main[y]) for x, y in R]
        c3 = realized(o3, arcs3, sorted(main.values()), Rb)
        if c3 < c2: fails.append(('step3 lost requests', t, c2, c3))
        # (4) the final enumeration is an enumeration of B_h: recount with all B_h arcs
        Ball = []
        for e in Bedges:
            u, v = tuple(e); Ball += [(u, v), (v, u)]
        c4 = realized(o3, Ball, sorted(main.values()), Rb)
        if c4 < c3: fails.append(('step4 lost requests', t, c3, c4))
        worst = max(worst, c4)
    return worst, fails, len(V), len(R)

if __name__ == '__main__':
    OPT_B = {1: 1, 2: 4, 3: 10}; UB_B = {4: 24, 5: 52, 6: 114}
    for h in [2, 3, 4, 5]:
        w, fails, nV, nR = run(h, trials=(400 if h <= 3 else 120), seed=h)
        ref = OPT_B.get(h) or UB_B[h]
        print(f"h={h}: |V(F_h)|={nV} |R|={nR}; pipeline max final count = {w} "
              f"[OPT/UB(B_h)={ref}, 3*2^h={3*2**h}]  failures: {len(fails)}"
              f"  {'OK' if not fails and w <= ref else '*** PROBLEM ***'}")
        for f_ in fails[:5]: print('    ', f_)
        sys.stdout.flush()

# ---------------------------------------------------------------------------
# Variant: instead of H = forward subgraph of a RANDOM enumeration (which only
# exercises 15 of the 24 achievable core port-relations), build H by choosing a
# core state independently per core, so that all 24 relations occur.
# ---------------------------------------------------------------------------
def core_state_list(G):
    from check_lemmas_2_3 import port_reach, acyclic
    arcs, inner = core_arcs(G, '0', 'a', 'b', 'l', 'r'); verts = PORTS + inner
    best = {}
    for mask in range(1 << len(arcs)):
        sub = [arcs[i] for i in range(len(arcs)) if (mask >> i) & 1]
        if not acyclic(sub, verts): continue
        rel = port_reach(sub, verts)
        if rel not in best or bin(mask).count('1') > bin(best[rel]).count('1'): best[rel] = mask
    return list(best.values()), arcs

def run_slots(h, trials, seed):
    V, A, M, cores, bases, f = build(G_NO, h)
    R = hypercube_requests(M, h)
    masks, absarcs = core_state_list(G_NO)
    rng = random.Random(seed); fails = []; worst = 0; seen = set(); ntested = 0
    for t in range(trials):
        Hs = set()
        for w, c in cores.items():
            m = rng.choice(masks)
            sub = {'a': c['ports']['a'], 'b': c['ports']['b'],
                   'l': c['ports']['l'], 'r': c['ports']['r']}
            tr = lambda x: sub[x] if x in sub else (x[0], w, x[2]) if isinstance(x, tuple) else x
            for i, (u, v) in enumerate(absarcs):
                if (m >> i) & 1:
                    uu = sub[u] if u in sub else f(('G', w, u[2]))
                    vv = sub[v] if v in sub else f(('G', w, v[2]))
                    Hs.add((uu, vv))
        for w, base in bases.items():
            (p, z), (z2, p2), (z3, q), (q2, z4) = base
            Hs.add(base[0] if rng.random() < .5 else base[1])
            Hs.add(base[2] if rng.random() < .5 else base[3])
        if topo(V, list(Hs)) is None:
            continue                       # not acyclic: skip (H must be acyclic)
        ntested += 1
        ok, w_, s = _pipeline(V, sorted(Hs), M, R, cores, bases, f)
        fails += ok; worst = max(worst, w_); seen |= s
    return worst, fails, ntested, len(seen)

def _pipeline(V, H, M, R, cores, bases, f):
    """the same pipeline as run(), factored out; returns (failures, final count, relations seen)"""
    fails = []; seen = set()
    Hs = set(H)
    c0 = count(V, H, M, R)
    arcs1 = [e for base in bases.values() for e in base if e in Hs]
    newV = set(); contract_pairs = []
    for w, c in cores.items():
        sub = [e for e in c['arcs'] if e in Hs]
        inv = {v: k for k, v in c['ports'].items()}
        ad = adj_of(sub); rel = set()
        for k, p in c['ports'].items():
            for q in reach(ad, p):
                if q in inv and q != p: rel.add((k, inv[q]))
        rel = frozenset(rel); seen.add(rel)
        if rel not in WIT:
            fails.append(('relation not representable', w, sorted(rel))); continue
        kind, oriented = WIT[rel]
        xw = ('x', w); yw = ('y', w); cw = ('c', w)
        nm = dict(c['ports']); nm.update({'x': xw, 'y': yw, 'c': cw})
        arcs1 += [(nm[u], nm[v]) for u, v in oriented]
        if kind == 'Q': newV |= {xw, yw}; contract_pairs.append((w, xw, yw, cw))
        else: newV.add(cw)
    V1 = (set(V) - {v for c in cores.values() for v in c['interior']}) | newV
    c1 = count(V1, arcs1, M, R)
    if c1 is None: fails.append(('step1 cyclic',)); return fails, 0, seen
    if c1 < c0: fails.append(('step1 lost', c0, c1))
    rep = {}
    for w, xw, yw, cw in contract_pairs: rep[xw] = cw; rep[yw] = cw
    g = lambda v: rep.get(v, v)
    arcs2 = {(g(u), g(v)) for u, v in arcs1 if g(u) != g(v)}
    V2 = {g(v) for v in V1}
    c2 = count(V2, arcs2, M, R)
    if c2 is None: fails.append(('step2 cyclic',)); return fails, 0, seen
    if c2 < c1: fails.append(('step2 lost', c1, c2))
    main = {('c', w): w for w in cores}
    for w, z in M.items(): main[z] = w
    subdiv = V2 - set(main) - {f(('A', '')), f(('B', ''))}
    out2 = defaultdict(list); inn2 = defaultdict(list)
    for u, v in arcs2: out2[u].append(v); inn2[v].append(u)
    for s in subdiv:
        if len(set(out2[s]) | set(inn2[s])) > 2: fails.append(('subdiv deg>2', s))
    arcs3 = {(main[u], main[v]) for s in subdiv for u in inn2[s] for v in out2[s]
             if u in main and v in main and u != v}
    Bedges = {frozenset(e) for w in cores for e in [(w, w+'0'), (w, w+'1'), (w+'0', w+'1')]}
    for u, v in arcs3:
        if frozenset((u, v)) not in Bedges: fails.append(('arc not B_h edge', u, v))
    o3 = topo(set(main.values()), arcs3)
    if o3 is None: fails.append(('step3 cyclic',)); return fails, 0, seen
    Rb = [(main[x], main[y]) for x, y in R]
    c3 = realized(o3, arcs3, sorted(main.values()), Rb)
    if c3 < c2: fails.append(('step3 lost', c2, c3))
    Ball = [a for e in Bedges for a in [tuple(e), tuple(e)[::-1]]]
    c4 = realized(o3, Ball, sorted(main.values()), Rb)
    if c4 < c3: fails.append(('step4 lost', c3, c4))
    return fails, c4, seen
