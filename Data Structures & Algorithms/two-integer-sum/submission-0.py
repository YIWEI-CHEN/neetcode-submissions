class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # diff -> idx
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], i]
            else:
                prev_map[num] = i