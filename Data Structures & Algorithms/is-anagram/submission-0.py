class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        base = ord('a')
        count1, count2 = [0] * 26, [0] * 26

        for i, c in enumerate(s):
            count1[ord(c) - base] += 1
            count2[ord(t[i]) - base] += 1
        
        matches = sum(1 for i in range(26) if count1[i] == count2[i])
        return matches == 26

