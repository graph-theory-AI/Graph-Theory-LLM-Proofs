/* Exhaustive search over all graphs on n vertices whose first c=n-k vertices form a
   clique (i.e. all graphs with a clique of order >= n-k, up to iso of the clique part),
   reporting non-exceptional 2-connected ones with eta < 2n and the minimum eta.
   usage: ./bigclique n k shard nshards                                              */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 24
static int n,c,k;
static unsigned adj[MAXN];
static int d[MAXN][MAXN];
static void bfs(int s){ for(int i=0;i<n;i++) d[s][i]=-1;
    int q[MAXN],h=0,t=0; q[t++]=s; d[s][s]=0;
    while(h<t){ int v=q[h++]; unsigned a=adj[v];
        while(a){ int u=__builtin_ctz(a); a&=a-1; if(d[s][u]<0){ d[s][u]=d[s][v]+1; q[t++]=u; } } } }
static int connected_skip(int skip){
    int start=-1; for(int i=0;i<n;i++) if(i!=skip){start=i;break;}
    unsigned seen=1u<<start, st=1u<<start; int cnt=1;
    while(st){ int v=__builtin_ctz(st); st&=st-1; unsigned a=adj[v]&~seen;
        if(skip>=0) a&=~(1u<<skip);
        while(a){ int u=__builtin_ctz(a); a&=a-1; seen|=1u<<u; st|=1u<<u; cnt++; } }
    return cnt==n-(skip>=0?1:0); }
static int two_connected(void){ if(!connected_skip(-1)) return 0;
    for(int v=0;v<n;v++) if(!connected_skip(v)) return 0; return 1; }
static long long eta(void){ for(int i=0;i<n;i++) bfs(i);
    long long W=0; for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) W+=d[i][j];
    long long Sz=0;
    for(int u=0;u<n;u++){ unsigned a=adj[u]&~((1u<<(u+1))-1);
        while(a){ int v=__builtin_ctz(a); a&=a-1; int nu=0,nv=0;
            for(int w=0;w<n;w++){ if(d[w][u]<d[w][v]) nu++; else if(d[w][v]<d[w][u]) nv++; }
            Sz+=(long long)nu*nv; } }
    return Sz-W; }
static int exceptional(void){ long long m=0; for(int i=0;i<n;i++) m+=__builtin_popcount(adj[i]); m/=2;
    long long full=(long long)n*(n-1)/2; if(m>=full-1) return 1;
    for(int v=0;v<n;v++) if(__builtin_popcount(adj[v])==2){ int ok=1;
        for(int i=0;i<n&&ok;i++){ if(i==v) continue; for(int j=i+1;j<n;j++){ if(j==v) continue;
            if(!((adj[i]>>j)&1)){ ok=0; break; } } } if(ok) return 1; }
    return 0; }
static long long best=-1, cnt=0, viol=0;
static int masks[MAXN];
static void build(int outmask){
    for(int i=0;i<n;i++) adj[i]=0;
    for(int i=0;i<c;i++) for(int j=i+1;j<c;j++){ adj[i]|=1u<<j; adj[j]|=1u<<i; }
    for(int i=0;i<c;i++){ unsigned m=masks[i];
        for(int t=0;t<k;t++) if((m>>t)&1){ adj[i]|=1u<<(c+t); adj[c+t]|=1u<<i; } }
    int bit=0;
    for(int i=0;i<k;i++) for(int j=i+1;j<k;j++){ if((outmask>>bit)&1){ adj[c+i]|=1u<<(c+j); adj[c+j]|=1u<<(c+i);} bit++; }
}
static void rec(int idx,int minmask,int shard,int nsh,int *sh){
    if(idx==c){
        int nout=1<<(k*(k-1)/2);
        for(int om=0;om<nout;om++){
            build(om);
            if(!two_connected()) continue;
            if(exceptional()) continue;
            cnt++;
            long long e=eta();
            if(best<0||e<best) best=e;
            if(e<2LL*n){ viol++; if(viol<=10){ printf("VIOLATION n=%d eta=%lld masks=",n,e);
                for(int i=0;i<c;i++) printf("%d,",masks[i]); printf(" out=%d\n",om); } }
        }
        return;
    }
    for(int m=minmask;m<(1<<k);m++){
        if(idx==0){ (*sh)++; if((*sh-1)%nsh!=shard) { masks[0]=m; continue; } }
        masks[idx]=m; rec(idx+1,m,shard,nsh,sh);
    }
}
int main(int argc,char**argv){ n=atoi(argv[1]); k=atoi(argv[2]); c=n-k;
    int shard=atoi(argv[3]), nsh=atoi(argv[4]); int sh=0;
    rec(0,0,shard,nsh,&sh);
    printf("n=%d k=%d shard=%d: graphs=%lld min-nonexceptional-eta=%lld 2n=%d below=%lld\n",n,k,shard,cnt,best,2*n,viol);
    return 0; }
