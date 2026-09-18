"""Exact check of Lemma 7's covariance formulas (21),(22) and variance bound (23)."""
from itertools import combinations
from fractions import Fraction as F

def stats(N):
    a=(N+1)//2; b=N//2
    V=list(range(N))
    subsets=list(combinations(V,a))
    tot=len(subsets)
    p=F(2*a*b,N*(N-1))
    # empirical probabilities
    def cross(S,e):
        u,v=e
        return (u in S) != (v in S)
    Ss=[set(s) for s in subsets]
    e0=(0,1)
    cnt=sum(1 for S in Ss if cross(S,e0))
    p_emp=F(cnt,tot)
    # adjacent pair (0,1),(0,2)
    f_adj=(0,2)
    cnt2=sum(1 for S in Ss if cross(S,e0) and cross(S,f_adj))
    p_adj=F(cnt2,tot)
    res={'N':N,'a':a,'b':b,'p':p,'p_emp':p_emp,'p_adj':p_adj,'p/2':p/2}
    cov_adj=p_adj-p*p
    res['cov_adj']=cov_adj
    res['cov_adj_le_1/N']=abs(cov_adj)<=F(1,N)
    if N>=4:
        f_dis=(2,3)
        cnt3=sum(1 for S in Ss if cross(S,e0) and cross(S,f_dis))
        p_dis=F(cnt3,tot)
        cov_dis=p_dis-p*p
        res['cov_dis']=cov_dis
        claimed = F(N,2*(N-1)**2*(N-3)) if N%2==0 else F(N+1,2*N*N*(N-2))
        res['cov_dis_claimed']=claimed
        res['cov_dis_matches']= cov_dis==claimed
        res['cov_dis_le_4/N^2']= cov_dis<=F(4,N*N)
        # joint prob formula claimed in text
        jf=F(4*a*(a-1)*b*(b-1),N*(N-1)*(N-2)*(N-3))
        res['joint_dis_formula_ok']= jf==p_dis
    return res

for N in range(3,11):
    r=stats(N)
    print(N, {k:(str(v)) for k,v in r.items() if k!='N'})
