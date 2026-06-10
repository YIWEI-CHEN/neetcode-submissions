from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def rob_line(values: List[int]) -> int:
            one_back, two_back = 0, 0
            for money in values:
                two_back, one_back = one_back, max(one_back, two_back + money)
            return one_back

        return max(rob_line(nums[0:-1]), rob_line(nums[1:]))
