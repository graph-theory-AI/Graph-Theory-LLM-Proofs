"""Structured exhaustive verification of the Section-4 reduction of
attacks_retry/2402.10782__01/output.md.

Full brute force over orderings is infeasible for the UNSAT instances (the
padding and private vertices admit astronomically many equally valid local
permutations), so instead we verify, exhaustively, every load-bearing finite
claim of the proof:

 (A) W is a matching covering EVERY variable-gadget vertex; Delta(B_sigma)=3;
     every wire spans >= 13 positions in sigma.
 (B) every wire is FORCED backward: the d=2 score-localisation intervals of its
     two endpoints are disjoint and in the sigma order  (this is the numerical
     form of step (8) of the writeup, and is stronger than its "moves by <=5"
     argument).
 (C) Lemma 2 for the ACTUAL gadget sizes m_x used: the only matchings of K_m
     hitting every directed triangle {z_i,z_{i+1},z_{i+2}} are M_0 and M_1,
     both of which are feedback arc sets.  (Hitting all those triangles is
     necessary for a FAS, and M_0,M_1 leave only one vertex uncovered, so the
     matching FASs of U_m are exactly M_0 and M_1.)
 (D) for EVERY truth assignment, B = W u (union of the chosen M_{t_x}) is a
     linear forest  <=>  the assignment satisfies Phi; and the explicit
     ordering of Section 4.5 realises exactly this B.
"""
import itertools, sys
from reduction import build, backward_graph, is_linear_forest, sat, ordering_from_assignment

def build_U(m):
    arc=[[False]*m for _ in range(m)]
    for i in range(m-1): arc[i+1][i]=True
    for i in range(m):
        for j in range(i+2,m): arc[i][j]=True
    return arc

def acyclic_after(arc,m,M):
    rem=set()
    for (a,b) in M: rem.add((a,b) if arc[a][b] else (b,a))
    indeg=[0]*m; out=[[] for _ in range(m)]
    for u in range(m):
        for v in range(m):
            if arc[u][v] and (u,v) not in rem: out[u].append(v); indeg[v]+=1
    st=[v for v in range(m) if indeg[v]==0]; seen=0
    while st:
        u=st.pop(); seen+=1
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0: st.append(v)
    return seen==m

def minimal_triangle_hitting_matchings(m):
    """All matchings of K_m that hit every triple {i,i+1,i+2}, enumerated so
    that every MINIMAL such matching is produced."""
    res=[]
    partner=[-1]*m
    def rec(i, edges):
        if i > m-3:
            res.append(frozenset(edges)); return
        tri=[i,i+1,i+2]
        hit=any(partner[a]==b for a in tri for b in tri if a<b)
        if hit: rec(i+1, edges); return
        for a,b in [(i,i+1),(i+1,i+2),(i,i+2)]:
            if partner[a]==-1 and partner[b]==-1:
                partner[a]=b; partner[b]=a
                rec(i+1, edges+[(a,b)])
                partner[a]=-1; partner[b]=-1
    rec(0, [])
    return res

def check_lemma2(m):
    arc=build_U(m)
    M0=frozenset((i,i+1) for i in range(0,m-2,2))
    M1=frozenset((i,i+1) for i in range(1,m-1,2))
    cands=set(minimal_triangle_hitting_matchings(m))
    # keep the minimal ones
    minimal=[M for M in cands if not any(N < M for N in cands)]
    ok = set(minimal)=={M0,M1}
    fas0=acyclic_after(arc,m,M0); fas1=acyclic_after(arc,m,M1)
    cov0=len({v for e in M0 for v in e}); cov1=len({v for e in M1 for v in e})
    return ok, fas0, fas1, cov0, cov1, len(minimal)

def main():
    all8=[[(0,s0),(1,s1),(2,s2)] for s0 in (True,False) for s1 in (True,False) for s2 in (True,False)]
    tests=[("SAT 1 clause", [[(0,True),(1,True),(2,True)]], 3),
           ("SAT 2 clauses", [[(0,True),(1,True),(2,True)],[(0,False),(1,False),(2,False)]], 3),
           ("UNSAT all 8 on x,y,z", all8, 3),
           ("SAT 7 of 8 (unique model)", all8[1:], 3),
           ("UNSAT 4 vars", all8+[[(0,True),(1,True),(3,True)]], 4),
           ("SAT 4 vars 6 clauses", [[(0,True),(1,True),(2,True)],[(0,False),(1,True),(3,True)],
                                     [(0,True),(2,False),(3,False)],[(1,False),(2,True),(3,True)],
                                     [(0,False),(1,False),(2,False)],[(1,True),(2,False),(3,True)]], 4)]
    lemma2_cache={}
    allok=True
    for label, formula, nvars in tests:
        n, arc, info = build(formula, nvars)
        gad=info['gadget']; W=info['W']; names=info['names']
        # (A)
        gadv={v for ids in gad.values() for v in ids}
        covered={v for e in W for v in e}
        A1 = gadv <= covered
        cnt={}
        for e in W:
            for v in e: cnt[v]=cnt.get(v,0)+1
        A2 = all(c==1 for c in cnt.values())
        Bs=backward_graph(arc,n,list(range(n)))
        deg={}
        for e in Bs:
            for v in e: deg[v]=deg.get(v,0)+1
        A3 = max(deg.values())
        A4 = min(max(e)-min(e) for e in W)
        # also: B_sigma == W u (gadget paths)
        paths={frozenset((ids[i],ids[i+1])) for ids in gad.values() for i in range(len(ids)-1)}
        A5 = (Bs == (set(W) | paths))
        # (B)
        outdeg=[sum(1 for v in range(n) if arc[u][v]) for u in range(n)]
        aa=[n-outdeg[v] for v in range(n)]
        lo=[max(1,aa[v]-2) for v in range(n)]; hi=[min(n,aa[v]+2) for v in range(n)]
        B1 = all(hi[min(e)] < lo[max(e)] for e in W)
        # (C)
        ms=sorted({len(ids) for ids in gad.values()})
        C=[]
        for m in ms:
            if m not in lemma2_cache: lemma2_cache[m]=check_lemma2(m)
            C.append((m,)+lemma2_cache[m])
        Cok=all(c[1] and c[2] and c[3] and c[4]==m_-1 and c[5]==m_-1
                for c in C for m_ in [c[0]])
        # (D)
        D_bad=[]
        for bits in itertools.product([False,True], repeat=nvars):
            B=set(W)
            for x in range(nvars):
                ids=gad[x]; m=len(ids); t=1 if bits[x] else 0
                Mt={frozenset((ids[i],ids[i+1])) for i in range(t, m-1, 2)}
                B |= Mt
            lf=is_linear_forest(B,n)
            s=all(any(bits[v]==sg for v,sg in cl) for cl in formula)
            if lf!=s: D_bad.append((bits,lf,s))
            if s:
                o=ordering_from_assignment(n,arc,info,bits)
                if backward_graph(arc,n,o)!=B: D_bad.append((bits,'ordering mismatch'))
        satisf = sat(formula,nvars) is not None
        ok = A1 and A2 and A3==3 and A4>=13 and A5 and B1 and Cok and not D_bad
        allok &= ok
        print(f"[{label}]  n={n}  gadget sizes={ms}  |W|={len(W)}  satisfiable={satisf}")
        print(f"   (A) W matching covering all gadget vertices: {A1 and A2}; "
              f"Delta(B_sigma)={A3}; min wire span={A4}; B_sigma == W u paths: {A5}")
        print(f"   (B) all {len(W)} wires forced backward by disjoint d=2 score intervals: {B1}")
        print(f"   (C) Lemma 2 for m in {ms}: " +
              "; ".join(f"m={c[0]}: minimal triangle-hitting matchings={c[5]} (=={{M0,M1}}: {c[1]}), "
                        f"M0,M1 are FAS: {c[2] and c[3]}, cover {c[4]}/{c[0]} vertices" for c in C))
        print(f"   (D) over all 2^{nvars} assignments, (W u matchings) is a linear forest "
              f"<=> assignment satisfies Phi: {not D_bad}" + (f"  BAD={D_bad[:3]}" if D_bad else ""))
        print(f"   => ALL CHECKS PASS: {ok}\n")
    print("OVERALL:", "ALL PASS" if allok else "FAILURE")

main()
