from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)
        self.vals = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.vals[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect_right(self.times.get(key, []), timestamp) - 1
        return "" if i < 0 else self.vals[key][i]