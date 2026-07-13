class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. restate
        2. straightforward
            2.1 count num freq, nums = [1,2,2,3,3,3], 
            freq = {
                1: 1
                2: 2
                3: 3
            }
            2.2 sort frequencies
            2.3 return top k elemnts
            2.3 n total num in arr; m distinct num; build freq -> O(n) time; sort -> O(mlogm); total O(n + mlogm);
            2.4 O(m) for freq map
        """

        counts = Counter(nums)
        sorted_counts = sorted(counts.keys(), key=lambda num: counts[num], reverse=True)
        return sorted_counts[:k]