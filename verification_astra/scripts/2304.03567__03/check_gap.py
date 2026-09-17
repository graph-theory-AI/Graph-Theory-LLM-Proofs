"""Lemma 6 + the gap (22): simulated annealing over enumerations of F_h built from a
NO-instance of two-linkage, testing whether the realized count can exceed
  (i) OPT(B_h)  [Lemma 6]        (ii) 3*2^h  [eq. (21)]
and, for comparison, the YES-instance value |R_h|."""
import random, sys, math
from collections import defaultdict
from construction import *

def make_eval(V,A,marked_list,R):
    Vl=list(V); idx={v:i for i,v in enumerate(marked_list)}
    def ev(order):
        pos={v:i for i,v in enumerate(order)}
        out=defaultdict(list)
        for u,v in A:
            if pos[u]<pos[v]: out[u].append(v)
        bits={}
        for v in reversed(order):
            b=1<<idx[v] if v in idx else 0
            for w in out.get(v,()): b|=bits[w]
            bits[v]=b
        c=0
        for x,y in R:
            if (bits[x]>>idx[y])&1 or (bits[y]>>idx[x])&1: c+=1
        return c
    return ev,Vl

def anneal(V,A,marked_list,R,iters,seed,T0=2.0,T1=0.02,init=None):
    ev,Vl=make_eval(V,A,marked_list,R)
    rng=random.Random(seed)
    order=list(init) if init else list(Vl)
    if init is None: rng.shuffle(order)
    cur=ev(order); best=cur; n=len(order)
    for it in range(iters):
        T=T0*(T1/T0)**(it/iters)
        i=rng.randrange(n); j=rng.randrange(n)
        if i==j: continue
        if rng.random()<0.5:
            order[i],order[j]=order[j],order[i]; undo=('s',i,j)
        else:
            v=order.pop(i); order.insert(j,v); undo=('m',j,i)
        val=ev(order)
        if val>=cur or rng.random()<math.exp((val-cur)/max(T,1e-9)):
            cur=val
            if val>best: best=val
        else:
            if undo[0]=='s': order[undo[1]],order[undo[2]]=order[undo[2]],order[undo[1]]
            else: v=order.pop(undo[1]); order.insert(undo[2],v)
    return best

if __name__=='__main__':
    OPT_B={1:1,2:4,3:10}            # exact (exhaustive, check_lemma7.py)
    UB_B ={4:24,5:52,6:114,7:244,8:516}  # DP upper bounds on OPT(B_h)
    for h in [3,4,5,7]:
        N=2**h; Rn=h*2**(h-1)
        Vn,An,Mn,_,_=build_F(G_NO,h); Rq=hypercube_requests(Mn,h); ml=sorted(Mn.values())
        iters = 120000 if h<=4 else (60000 if h==5 else 12000)
        restarts = 8 if h<=4 else (4 if h==5 else 2)
        best=0
        for s in range(restarts):
            best=max(best,anneal(Vn,An,ml,Rq,iters,seed=100*h+s))
        ref = OPT_B.get(h) or UB_B[h]
        kind= 'OPT(B_h)' if h in OPT_B else 'UBound(B_h)'
        print(f"h={h}: |V(F_h)|={len(Vn)} |R|={Rn}  best NO-instance value found = {best}"
              f"   [{kind}={ref}, 3*2^h={3*N}]  "
              f"{'OK (<= both)' if best<=ref and best<=3*N else '*** EXCEEDS ***'}")
        sys.stdout.flush()
