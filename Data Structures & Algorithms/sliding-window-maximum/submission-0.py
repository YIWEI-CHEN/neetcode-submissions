from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        candidates = deque()
        ans = []
        for right, val in enumerate(nums):
            while candidates and candidates[0] <= right - k:
                candidates.popleft()
            while candidates and nums[candidates[-1]] <= val:
                candidates.pop()
            candidates.append(right)
            if right >= k - 1:
                ans.append(nums[candidates[0]])
        return ans