from typing import List
from collections import defaultdict

class DSU:
    def __init__(self):
        self.parent = {}
    def find(self, x: str) -> str:
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: str, b: str) -> None:
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.parent[root_b] = root_a

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        email_to_name = {}
        groups = defaultdict(list)

        for account in accounts:
            name, first = account[0], account[1]
            email_to_name[first] = name
            for email in account[1:]:
                email_to_name[email] = name
                dsu.union(first, email)
        
        for email in email_to_name:
            groups[dsu.find(email)].append(email)
        
        result = []
        for root, emails in groups.items():
            result.append([email_to_name[root]] + sorted(emails))
        
        return result
        