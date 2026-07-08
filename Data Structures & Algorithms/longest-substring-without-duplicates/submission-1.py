class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        valid substring: no duplicate chars
        sliding widnows with left and right pointers
        hash map to track last indx of each chars in the windows
        jump left pointer to one position after prev occurance
        s = abcabc
        abc, best =3
        right -> 'a', repeating, jump left =1
        next 'b' repeated, jump left to 1 + 1 = 2
        Time: O(n) total char
        Space: O(k) distinct char
        """
        last_seen = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last_seen:
                # jump left pointer
                left = max(left, last_seen[ch] + 1)
            last_seen[ch] = right
            best = max(best, right - left + 1)
        return best
