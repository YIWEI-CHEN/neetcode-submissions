from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        1. valid substring, two distinct chars
        2. sliding window, left, right pointer
        3. hash map for char freq
        4. O(n), n total chars in s
        """
        left = 0
        best = 0
        counts = defaultdict(int)
        for right, char in enumerate(s):
            counts[char] += 1

            while len(counts) > 2:
                left_char = s[left]
                counts[left_char] -= 1

                if counts[left_char] == 0:
                    del counts[left_char]
                
                left += 1
            
            best = max(best, right - left + 1)

        """
        s = eceba
        "e" valid, best = 1
        "ec", valid, best = 2
        "ece", valid, best = 3
        "eceb", invalid, -> shrink, "eb", its 2, best = 3
        "eba", invliad -> shrink "ba", its 2, best = 3
        return 3 (ece)
        """

        return best