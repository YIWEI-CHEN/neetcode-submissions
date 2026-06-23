"""
1. Disjoint Set Union (DSU) track which nodes belong to the same group, by checking its root
    `find`: find the root of a node
    `union(a, b)`: makes b's root point to a's root
2. Track emails' group by DSU. If emails are in the same group, they are shared by an account.
"""
from collections import defaultdict

class DSU:
    def __init__(self):
        self.parent = {} # tracking node x's root
    
    def find(self, x: str) -> str:
        # init x'root by itself
        if x not in self.parent:
            self.parent[x] = x  # root node
        # x's root is other node, not itself
        if self.parent[x] != x:
            """
            example: c → b → a → a  (root)
            before path compression: c -> b; b -> a
            after: c -> a; b -> a
            """
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    
    def union(self, a: str, b: str) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_b] = root_a


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        email_to_name = {}

        for account in accounts:
            name, first = account[0], account[1]
            email_to_name[first] = name
            for email in account[1:]:
                email_to_name[email] = name
                dsu.union(first, email)
        
        # group emails by their roots
        groups = defaultdict(list)
        for email in email_to_name:
            groups[dsu.find(email)].append(email)
        
        res = []
        for root, emails in groups.items():
            res.append([email_to_name[root]] + sorted(emails))
        return res

