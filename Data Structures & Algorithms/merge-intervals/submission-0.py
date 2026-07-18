class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        start time of interval
        start time of next interval is earlier of end time of other intervals, 
        => merge 
        [1, 3] start = 1, end = 5,
        [1, 5] start = 1
        since 2nd start is earlier than (less than) end of [1, 3]
        merge [1, 3] and [1, 5] together

        sort start time of all interval
        Time O(nlogn)
        Space O(output) |merged|
        """
        intervals.sort(key=lambda interval: interval[0])
        merged = []

        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged
