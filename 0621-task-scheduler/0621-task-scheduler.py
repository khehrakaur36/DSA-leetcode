import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq ={}
        for ch in range(len(tasks)):
            freq[tasks[ch]]= freq.get(tasks[ch],0)+1
        heap =[]
        for count in freq.values():
            heapq.heappush(heap, -count)
        
        q = deque() 
        time =0
        while heap or q:
            time+=1

            if heap:
                count = heapq.heappop(heap)
                count+=1

                if count != 0:
                    q.append((count, time+n))    
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time                