from bisect import bisect_right
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)
        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.vals[key].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        times = self.times[key]
        if not times:
            return ""
        idx = bisect_right(times, timestamp) - 1

        return "" if idx < 0 else self.vals[key][idx]
