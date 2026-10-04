from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        ends, dp = [], [0]
        for end, start, p in jobs:
            i = bisect_right(ends, start)
            dp.append(max(dp[-1], p + dp[i]))
            ends.append(end)
        return dp[-1]
