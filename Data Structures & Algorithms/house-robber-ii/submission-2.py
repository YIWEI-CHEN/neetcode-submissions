class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        split circle to two linear: (1) exclude the last house (2) exclude the first house
        nums = [2, 3, 2]
        exclude last = [2, 3] -> max = 3
        exclude first = [3, 2] -> max = 3
            => ans max([2, 3], [3, 2])
        ans = max(case1, case2)
        dp[i] = max(skip or rob)
        skip = dp[i - 1]
        rob = money + dp[i - 2]
        -> dp[i] = max(dp[i - 1], num[i] + dp[i -2 ])
                       |                 |
                       one_back          two_back
        edge case
        nums = [2], no need to split 
        Time: O(2n) = O(n); Space = O(2) = O(1)
        """
        if len(nums) == 1:
            return nums[0]
        
        # linear dp
        def dp(houses: List[int]) -> int:
            one_back = two_back = 0
            for money in houses:
                two_back, one_back = one_back, max(one_back, money + two_back)
            return one_back
        
        return max(dp(nums[:-1]), dp(nums[1:]))

            