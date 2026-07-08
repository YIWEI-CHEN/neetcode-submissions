class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        best = 0
        counts = defaultdict(int)
        for right, right_chr in enumerate(s):
            counts[right_chr] += 1

            while len(counts) > 2:
                left_chr = s[left]
                counts[left_chr] -= 1
                if counts[left_chr] == 0:
                    del counts[left_chr]
                left += 1
            
            best = max(best, right - left + 1)
        
        return best



