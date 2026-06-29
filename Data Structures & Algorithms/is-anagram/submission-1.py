class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. anagram: char appears the same times
        2. if len differnt, false
        3. walk through strings
        4. increment count in s, decrement count in t. if all counts == 0, freq match
        5. Time O(n), n is |s| Space: O(26) = O(1)
        """
        if len(s) != len(t):
            return False
        counts = [0] * 26
        base = ord('a')
        for i, c in enumerate(s):
            counts[ord(c) - base] += 1
            counts[ord(t[i]) - base] -= 1
        
        return all(count == 0 for count in counts)
