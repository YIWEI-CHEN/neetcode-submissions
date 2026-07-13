from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        nums = [1,2,2,3,3,3], k = 2
        1: 1
        2: 2
        3: 3
        return 3, 2
        Counter(nums) -> num freq
        bucket sort to find top freq elements
        put the num with the same count in a bucket
        nums = [1,2,2,2,3,3,3]
        bucekt 1, 2, 3
               1     3,
                     2
        scan the buckets
        append 3, 2 until k
        Time O(n)
        Space O(n)
        """
        counts = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        """
        bucekt 1, 2, 3
               1     3,
                     2
        """
        for val, count in counts.items():
            buckets[count].append(val)
        
        res = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                if len(res) < k:
                    res.append(num)
        
        return res