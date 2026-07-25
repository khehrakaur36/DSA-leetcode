import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap =[]
        min_heap =[]
        #store
        for c , p in zip(capital, profits):
            heapq.heappush(min_heap, (c,p))
        #Repeat k times
        for i in range(k):
            #affordable
            while min_heap and min_heap[0][0]<=w:
                c,p = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -p) #max heap

            #no affordable
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)
        return w    
