/* Simulated annealing over 2-connected graphs on n vertices, minimizing eta(G)-2n.
   Reports every non-exceptional 2-connected graph found with eta < 2n, and the
   overall minimum of eta over non-exceptional 2-connected graphs visited.
   usage: ./anneal n seed iters restarts                                        */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAXN 32
static int n;
static unsigned long long adj[MAXN];
static int d[MAXN][MAXN];

static unsigned long long rstate;
static double rnd(void){ rstate ^= rstate<<13; rstate ^= rstate>>7; rstate ^= rstate<<17;
    return (double)(rstate>>11)/9007199254740992.0; }
static int rnd_int(int k){ return (int)(rnd()*k); }

static void bfs(int s){
    for(int i=0;i<n;i++) d[s][i]=-1;
    int q[MAXN],h=0,t=0; q[t++]=s; d[s][s]=0;
    while(h<t){ int v=q[h++]; unsigned long long a=adj[v];
        while(a){ int u=__builtin_ctzll(a); a&=a-1;
            if(d[s][u]<0){ d[s][u]=d[s][v]+1; q[t++]=u; } } }
}
static int connected_skip(int skip){
    int start=-1; for(int i=0;i<n;i++) if(i!=skip){start=i;break;}
    unsigned long long seen=1ULL<<start, stack=1ULL<<start;
    int cnt=1;
    while(stack){ int v=__builtin_ctzll(stack); stack&=stack-1;
        unsigned long long a=adj[v]&~seen; if(skip>=0) a&=~(1ULL<<skip);
        while(a){ int u=__builtin_ctzll(a); a&=a-1; seen|=1ULL<<u; stack|=1ULL<<u; cnt++; } }
    return cnt == n-(skip>=0?1:0);
}
static int two_connected(void){
    if(!connected_skip(-1)) return 0;
    for(int v=0;v<n;v++) if(!connected_skip(v)) return 0;
    return 1;
}
static long long eta(void){
    for(int i=0;i<n;i++) bfs(i);
    long long W=0; for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) W+=d[i][j];
    long long Sz=0;
    for(int u=0;u<n;u++){ unsigned long long a=adj[u]&~((u==63)?0:((1ULL<<(u+1))-1));
        while(a){ int v=__builtin_ctzll(a); a&=a-1;
            int nu=0,nv=0;
            for(int w=0;w<n;w++){ if(d[w][u]<d[w][v]) nu++; else if(d[w][v]<d[w][u]) nv++; }
            Sz+=(long long)nu*nv; } }
    return Sz-W;
}
static int exceptional(void){
    long long m=0; for(int i=0;i<n;i++) m+=__builtin_popcountll(adj[i]); m/=2;
    long long full=(long long)n*(n-1)/2;
    if(m>=full-1) return 1;
    for(int v=0;v<n;v++) if(__builtin_popcountll(adj[v])==2){
        int ok=1;
        for(int i=0;i<n&&ok;i++){ if(i==v) continue;
            for(int j=i+1;j<n;j++){ if(j==v) continue;
                if(!((adj[i]>>j)&1)){ ok=0; break; } } }
        if(ok) return 1; }
    return 0;
}
static void g6print(void){
    char buf[256]; int p=0; buf[p++]=(char)(n+63);
    int bit=0,cur=0;
    for(int j=1;j<n;j++) for(int i=0;i<j;i++){
        cur=(cur<<1)|(int)((adj[i]>>j)&1); bit++;
        if(bit==6){ buf[p++]=(char)(cur+63); bit=0; cur=0; } }
    if(bit){ cur<<=(6-bit); buf[p++]=(char)(cur+63); }
    buf[p]=0; printf("%s",buf);
}
int main(int argc,char**argv){
    n=atoi(argv[1]); rstate=strtoull(argv[2],0,10)|1;
    long iters=atol(argv[3]); int restarts=atoi(argv[4]);
    long long best=-1; unsigned long long bestadj[MAXN];
    long long found=0;
    for(int rs=0;rs<restarts;rs++){
        /* random 2-connected start: hamiltonian cycle + random extra edges */
        double p=0.05+0.85*rnd();
        for(int i=0;i<n;i++) adj[i]=0;
        for(int i=0;i<n;i++){ int j=(i+1)%n; adj[i]|=1ULL<<j; adj[j]|=1ULL<<i; }
        for(int i=0;i<n;i++) for(int j=i+1;j<n;j++)
            if(!((adj[i]>>j)&1) && rnd()<p){ adj[i]|=1ULL<<j; adj[j]|=1ULL<<i; }
        long long cur=eta();
        double T=8.0;
        for(long it=0; it<iters; it++){
            T = 0.05 + 8.0*(1.0-(double)it/iters);
            int i=rnd_int(n), j=rnd_int(n); if(i==j) continue;
            adj[i]^=1ULL<<j; adj[j]^=1ULL<<i;
            if(!two_connected()){ adj[i]^=1ULL<<j; adj[j]^=1ULL<<i; continue; }
            long long ne=eta();
            double dE=(double)(ne-cur);
            if(dE<=0 || rnd()<exp(-dE/T)){
                cur=ne;
                if(!exceptional()){
                    if(best<0||cur<best){ best=cur; memcpy(bestadj,adj,sizeof adj); }
                    if(cur<2LL*n){ found++; if(found<=20){ printf("BELOW n=%d eta=%lld g6=",n,cur); g6print(); printf("\n"); } }
                }
            } else { adj[i]^=1ULL<<j; adj[j]^=1ULL<<i; }
        }
    }
    memcpy(adj,bestadj,sizeof adj);
    printf("n=%d best-nonexceptional-eta=%lld 2n=%d 3n-10=%d below2n=%lld g6=",n,best,2*n,3*n-10,found);
    g6print(); printf("\n");
    return 0;
}
