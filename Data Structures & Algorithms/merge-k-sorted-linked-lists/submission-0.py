# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappop, heappush

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(0)
        tail = dummy
        order = 0  # tie breaker

        # inser the head of lists to the heap
        for node in lists:
            if node:
                heappush(heap, (node.val, order, node))
                order += 1
        
        while heap:
            _, _, node = heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heappush(heap, (node.next.val, order, node.next))
                order += 1
            
        return dummy.next
