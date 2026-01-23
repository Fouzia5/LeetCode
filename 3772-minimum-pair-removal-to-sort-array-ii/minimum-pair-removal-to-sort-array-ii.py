import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n=len(nums)
        if n<2:
            return 0
        val=nums[:]
        l=[i-1 for i in range(n)]
        r=[i+1 for i in range(n)]
        r[n-1]=-1
        alive=[1]*n
        bad=0
        for i in range(n-1):
            if val[i]>val[i+1]:
                bad+=1
        pq=[]
        vid=0
        pid=[0]*n
        for i in range(n-1):
            heapq.heappush(pq,(val[i]+val[i+1],i,vid))
            pid[i]=vid
            vid+=1
        ops=0
        while bad>0:
            s,i,pi=heapq.heappop(pq)
            if not alive[i]:
                continue
            j=r[i]
            if j==-1 or not alive[j]:
                continue
            if pid[i]!=pi:
                continue
            li=l[i]
            rj=r[j]
            if li!=-1 and val[li]>val[i]:
                bad-=1
            if val[i]>val[j]:
                bad-=1
            if rj!=-1 and val[j]>val[rj]:
                bad-=1
            val[i]+=val[j]
            alive[j]=0
            r[i]=rj
            if rj!=-1:
                l[rj]=i
            if li!=-1 and val[li]>val[i]:
                bad+=1
            if rj!=-1 and val[i]>val[rj]:
                bad+=1
            pid[i]=vid
            if r[i]!=-1:
                heapq.heappush(pq,(val[i]+val[r[i]],i,vid))
                vid+=1
            if li!=-1:
                pid[li]=vid
                heapq.heappush(pq,(val[li]+val[i],li,vid))
                vid+=1
            ops+=1
        return ops
