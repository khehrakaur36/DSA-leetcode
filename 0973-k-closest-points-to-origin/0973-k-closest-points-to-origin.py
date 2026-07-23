import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap =[]
        for x, y in points:
            distt = x*x + y*y
            heapq.heappush(heap , (-distt,[x, y]))

            if len(heap)>k:
                heapq.heappop(heap)
        return [point for distt, point in heap ]        