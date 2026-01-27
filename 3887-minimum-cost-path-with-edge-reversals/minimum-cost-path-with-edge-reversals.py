import heapq

class Solution:
    def minCost(self, n, edges):
        outg=[[] for _ in range(n)]
        inc=[[] for _ in range(n)]
        for u,v,w in edges:
            outg[u].append((v,w))
            inc[v].append((u,w))
        INF=10**30
        dist=[INF]*(2*n)
        h=[]
        dist[0]=0
        h.append((0,0))
        while h:
            d,x=heapq.heappop(h)
            if d!=dist[x]:
                continue
            u=x//2
            s=x%2
            if u==n-1:
                return d
            for v,w in outg[u]:
                y=2*v
                nd=d+w
                if nd<dist[y]:
                    dist[y]=nd
                    heapq.heappush(h,(nd,y))
            if s==0:
                for v,w in inc[u]:
                    y=2*v
                    nd=d+2*w
                    if nd<dist[y]:
                        dist[y]=nd
                        heapq.heappush(h,(nd,y))
                y=2*u+1
                if d<dist[y]:
                    dist[y]=d
                    heapq.heappush(h,(d,y))
        return -1
