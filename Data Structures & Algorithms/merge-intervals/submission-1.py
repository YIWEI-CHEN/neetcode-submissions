class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        merged = []
        
        for start, end in intervals:
            # we need to add an interval to the merged list
            # start of current > end time of last elements in the merged list
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(end, merged[-1][1])
        
        return merged