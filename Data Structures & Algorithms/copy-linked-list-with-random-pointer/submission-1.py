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
        1. Maintain a old_to_new dict to map old nodes to new nodes, due to random attribute
        2. iterate old nodes to init old_to_new dict
        3. iterate again to assign next and random nodes.
        """
        if not head:
            return None

        old_to_new = {}
        # pointer to iterate the linked list
        node = head
        while node:
            old_to_new[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            clone = old_to_new[node]
            clone.next = old_to_new.get(node.next)
            clone.random = old_to_new.get(node.random)
            node = node.next
        
        return old_to_new[head]
