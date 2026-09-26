# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        order = 0

        for node in lists:
            if node:
                heappush(heap, (node.val, order, node))
                order += 1
        
        dummy = ListNode(0)
        tail = dummy

        while heap:
            _, _, node = heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heappush(heap, (node.next.val, order, node.next))
                order += 1
            
        return dummy.next
        