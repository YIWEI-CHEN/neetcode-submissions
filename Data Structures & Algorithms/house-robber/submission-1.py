class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        1. dynamic problem
        2. rob house[i], get money and best from two house ago
           skip, get best from one house ago
           dp[i] = max(dp[i - 1], money[i] + dp[i -2])
                        |                  |
                        skip               rob
        3. two_back: best from two houses ago
           one_back: best from prev house
           eg., nums[2, 7, 9, 3]
            house 0: max(0, 0+2) = 2
            house 1: max(2, 0+7) = 7
            house 2: max(7, 2+9) = 11
            house 3: max(11, 7+3) = 10
        4. Time: O(n); Space: O(1)
        """
        two_back = one_back = 0
        for money in nums:
            best = max(one_back, two_back + money)
            # update status
            two_back, one_back = one_back, best
        return one_back
            