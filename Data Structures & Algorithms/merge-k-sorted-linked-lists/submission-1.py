# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappop, heappush
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        1. Maintain a min-heap to trace the min head of each list
        2. pop a node from the heap, and append to the new head
        3. python heap need to have tie breaker when two node.vals are same 
        """
        # min-heap
        heap = []
        order = 0  # tie breaker

        # push head of lists to the min-heap
        for node in lists:
            if node:
                heappush(heap, (node.val, order, node))
                order += 1
        
        # new head
        dummy = ListNode(0)
        # pointer to the current postion
        tail = dummy
        
        # pop heap to the new head
        while heap:
            _, _, node = heappop(heap)
            tail.next = node
            tail = tail.next

            # add the next node to the min-heap
            if node.next:
                heappush(heap, (node.next.val, order, node.next))
                order += 1
        
        return dummy.next
            
