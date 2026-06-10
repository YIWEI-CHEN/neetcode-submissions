class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        two_back, one_back = 0, 0
        for money in nums:
            two_back, one_back = one_back, max(one_back, two_back + money)
        return one_back
