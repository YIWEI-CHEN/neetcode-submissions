from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for num, freq in Counter(nums).items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
        return [num for _, num in heap]