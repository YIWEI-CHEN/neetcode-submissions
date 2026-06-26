class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] = max(num[i] + dp[i - 2], dp[i - 1])
        state var: one_back, two_back
        [1, 1, 3, 3]
        house 0: max(1, 0) = 1, one_back = 1, two_back = 0
        house 1: max(1, 1+0) = 1, one_back= 1, two_back = 1
        house 2: max(1, 1 + 3) = 4, one_back=4, two_back = 1
        house 3: max(4, 1 +3) = 4, one_back=4, two_back=4
        return 4
        Time: O(n); Space O(1)
        """
        one_back = two_back = 0
        for money in nums:
            two_back, one_back = one_back, max(one_back, two_back + money)
        return one_back