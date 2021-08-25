import heapq
import math


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances=[]
        for i,(x1,y1) in enumerate(workers):
            distances.append([])
            for j,(x2,y2) in enumerate(bikes):
                distances[-1].append((abs(x1-x2)+abs(y1-y2),i,j))
            distances[-1].sort(reverse=True)
        ans=[-1]*len(workers)
        used_bikes=set()
        q=[distances[i].pop() for i in range(len(workers))]
        heapq.heapify(q)
        res=0
        while len(used_bikes)<len(workers):
            dist,worker,bike=heapq.heappop(q)
            if bike not in used_bikes:
                res+=dist
                ans[worker]=bike
                used_bikes.add(bike)
            else:
                heapq.heappush(q,distances[worker].pop())
        return res




