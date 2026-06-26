"""
vals[key] = value
times[key] = timestamp
set O(1)
get binary search latest timestamp
binary search right, insert position, that is equal to or bigger to current val
right_idx - 1 -> latest timestamp
Time get = O(logM), m is key size
Space: O(total sets)
"""
from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)
        self.times = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append(value)
        self.times[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        times = self.times.get(key)
        if not times:
            return ""
        idx = bisect_right(times, timestamp) - 1
        if idx >= 0:
            return self.vals[key][idx]
        return ""
        
