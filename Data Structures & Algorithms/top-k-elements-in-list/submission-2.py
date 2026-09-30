from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)

        ans = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans