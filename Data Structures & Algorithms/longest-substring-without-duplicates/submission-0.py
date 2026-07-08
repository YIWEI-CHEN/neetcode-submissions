class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        valid subtring, no repeating charaters
        hash map = last index for each char
        jump left pointer to one postion after prev occurance
        eg:
        s=abcabc
        abc -> best 3
        next a -> repeat 'a', move left to 1
        next b repeated, move left to 2, idx of 'b' + 1
        """
        left = 0
        best = 0
        last_seen = {}
        for right, right_char in enumerate(s):
            if right_char in last_seen:
                # jump left char
                left = max(left, last_seen[right_char] + 1)
            last_seen[right_char] = right
            best = max(best, right - left + 1)
        return best
