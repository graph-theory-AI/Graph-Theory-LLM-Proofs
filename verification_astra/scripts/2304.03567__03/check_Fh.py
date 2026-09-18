"""Check size formula (8), Lemma 4 (strong connectivity), Lemma 5 (YES => OPT=|R|),
and |R_h| = h 2^{h-1}."""
from construction import *
from collections import defaultdict

def lemma5_path(G,h):
    """Explicitly build the a->b directed path through all marked vertices (Lemma 5)."""
    # recursive: path(w,d) returns list of vertices from A_(w) to B_(w)
    def P(w,d):
        if d==0: return [('A',w),('Z',w),('B',w)]
        g=lambda v:('G',w,v)
        left=P(w+'0',d-1); right=P(w+'1',d-1)
        # a -> s1 ~> t1 -> ell(=A_{w0}) ... b^{w0}=a^{w1} ... r(=B_{w1}) -> s2 ~> t2 -> b
        # G_YES: s1->t1 and s2->t2 directly
        head=[('A',w), g('s1'), g('t1')]
        tail=[g('s2'), g('t2'), ('B',w)]
        return head + left + right[1:] + tail   # right[0]==B_{w0}==A_{w1} identified
    return P('',h)

for h in range(0,8):
    for name,G in [('NO',G_NO),('YES',G_YES)]:
        V,A,M,a,b=build_F(G,h)
        n=len(G['V'])
        pred=(n+4)*2**h-(n+1)
        R=hypercube_requests(M,h)
        strong=is_strong(V,A)
        ok_size = (len(V)==pred)
        line=f"h={h} {name}: |V|={len(V)} (formula {pred}) {'OK' if ok_size else 'MISMATCH'}; |A|={len(A)}; |R|={len(R)} (h2^(h-1)={h*2**(h-1) if h else 0}); strong={strong}"
        print(line)
        assert ok_size and strong
        if name=='YES':
            dsu_V,dsu_A,dsu_M,_,_=V,A,M,a,b
            p=lemma5_path(G,h)
            # canonicalise through the same identification used in build_F
            # rebuild dsu mapping by matching names
            # (build_F returns representatives; re-derive by re-running with a map)
            # simplest: verify path via a fresh build that exposes the find map
            import construction as C
            dsu=C.DSU()
            def rec(w,d):
                if d>0:
                    rec(w+'0',d-1); rec(w+'1',d-1)
                    dsu.union(('B',w+'0'),('A',w+'1'))
            rec('',h)
            f=dsu.find
            pq=[f(x) for x in p]
            assert len(set(pq))==len(pq), ('path not simple at h=%d'%h, len(pq), len(set(pq)))
            Aset=set(A)
            for u,v in zip(pq,pq[1:]):
                assert (u,v) in Aset, ('missing arc',u,v)
            assert set(M.values())<=set(pq), 'path misses a marked vertex'
            # order: path first, then everything else
            order=pq+[v for v in V if v not in set(pq)]
            got=realized(order,A,sorted(M.values()),R)
            print(f"      Lemma 5: path length {len(pq)}, contains all {len(M)} marked vertices, realized={got}/{len(R)} {'OK' if got==len(R) else 'FAIL'}")
            assert got==len(R)
print("\nAll size / strong-connectivity / Lemma-5 checks passed.")
