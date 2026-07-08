from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        valid substring, at most k distinct char
        sliding window, 
        check char freq and dist chars in the windows, at most k, bigger than, shrink slide from the left
        hash map, dict, key = char, value = count
        slide, check lenght of substring, best 
        """
        if k == 0:
            return 0
        
        left = 0
        best = 0
        counts = defaultdict(int)
        for right, char in enumerate(s):
            counts[char] += 1

            while len(counts) > k:
                left_char = s[left]
                counts[left_char] -= 1

                if counts[left_char] == 0:
                    del counts[left_char]
                left += 1
                
            best = max(best, right - left + 1)
        
        return best