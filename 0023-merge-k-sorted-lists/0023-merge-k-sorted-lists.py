# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class Node:
            def __init__(self, val, next):
                self.val = val
                self.next = next
            def __lt__(self, others):
                return self.val< others.val
        heap =[]
        for node in lists:
            if node:
                heapq.heappush(heap, Node(node.val, node))

        dummy = ListNode(0)
        curr = dummy          
        while heap:
            smallest = heapq.heappop(heap)        
            curr.next = smallest.next
            curr = curr.next
            if smallest.next.next:
                heapq.heappush(heap, Node(smallest.next.next.val, smallest.next.next))
        return dummy.next
