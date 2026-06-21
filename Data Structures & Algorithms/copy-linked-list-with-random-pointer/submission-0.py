"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        1. due to random node, we need to have a dict to map old node to new node
        2. iterate old list to create new node and maintain the map
        3. iterate the old list 2nd time to point to random node 
        """
        if not head:
            return None
        
        old_to_new = {None: None}
        node = head
        while node:
            old_to_new[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            clone = old_to_new[node]
            clone.next = old_to_new[node.next]
            clone.random = old_to_new[node.random]
            node = node.next

        return old_to_new[head]